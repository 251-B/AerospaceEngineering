clear all
close all
clc

%% Initialise simulation variables
U = 1;
alpha = 0.1;
k = 0.5;
tmax = 20;                      % Maximum simulation time
t_report = [1 5 15];            % Times plotted in the report
% Boundary condition for the animation: 'Dirichlet', 'Neumann' or 'Periodic'
BC = 'Periodic';
animate = false;                % true: play the animation (not in -batch runs)

Nx = 201;                       % Grid size (number of points)
Dx = 20/(Nx-1);                 % Spacing between points

% Maximum timestep that satisfies stability conditions (Eq. 6)
Dt1 = 0.5*Dx/U;
Dt2 = 0.5*Dx^2/alpha;

Dt = min([Dt1, Dt2]);           % Timestep

% Extension (not in the guidelines): the von Neumann analysis of FTCS
% requires D <= 1/2 AND C^2 <= 2D. Eq. (6) alone does not guarantee
% stability when U >> alpha.
C = U*Dt/Dx;
D = alpha*Dt/Dx^2;
assert(D <= 0.5 + 1e-12 && C^2 <= 2*D + 1e-12, ...
    'FTCS unstable: C^2 = %.3g, 2D = %.3g', C^2, 2*D);

x = -10:Dx:10;                  % Space array (contains position of grid points)
t = 0:Dt:tmax;                  % Time array (from 0 to tmax)
Nt = length(t);

% Initial condition (Eq. 2)
f0 = sech(k*(x+2)).^2;

%% Finite differences simulation
BCs = {'Dirichlet', 'Neumann', 'Periodic'};
for b = 1:numel(BCs)
    F.(BCs{b}) = simulate(f0, U, alpha, Dx, Dt, Nt, BCs{b});
end

%% Checks
fprintf('Dt = %.4g, Nt = %d, C = %.3g, D = %.3g\n', Dt, Nt, C, D);
for b = 1:numel(BCs)
    f = F.(BCs{b});
    assert(all(isfinite(f(:))), '%s: non-finite values', BCs{b});
    M = Dx*sum(f(1:Nx-1,:), 1);                 % Integral of f over one period
    fprintf('%-9s  M(0) = %.4f  M(%g) = %.4f\n', BCs{b}, M(1), tmax, M(end));
    for m = 1:numel(t_report)
        n = find(t >= t_report(m) - Dt/2, 1);
        [fmax, imax] = max(f(:,n));
        fprintf('           t = %4.1f  max f = %.3f at x = %6.2f\n', t(n), fmax, x(imax));
    end
end
fprintf('Periodic   max |f(1)-f(Nx)| = %.2e\n', max(abs(F.Periodic(1,:) - F.Periodic(Nx,:))));

%% Plot dynamic graph
if animate
    f = F.(BC);
    % Initialise plot
    fig=figure(1);
    clf
    axfig = gca;
    axfig.FontSize = 16;
    hold on
    box on
    grid on
    axfig.XLim = [-10 10];
    axfig.YLim = [-0.5 1.0];
    axfig.TickLabelInterpreter = 'latex';
    xlabel('$x$', 'Interpreter', 'latex');
    ylabel('$f$', 'Interpreter', 'latex', 'rotation', 0);
    p = plot(0,0);      % Dummy plot (gets deleted afterwards)

    % Plot curves
    for n = 1:30:Nt
        delete(p);                                                          % Delete previous curve
        p = plot(x, f(:,n), '.k-');                                         % Plot the wave
        title(['$t = \ $'  num2str(t(n), '%2.2f')] , 'Interpreter', 'latex')  % Update title with the time
        pause(0.1)                                                          % Pause time (secs) between consecutive graphs
    end
end

%% Plot graph for report
outdir = fileparts(mfilename('fullpath'));
if isempty(outdir)
    outdir = pwd;
end
styles = {'-', '--', ':'};
report = {'Neumann', 'fig_neumann'; 'Periodic', 'fig_periodic'};

for b = 1:size(report, 1)
    fig = figure('Units', 'centimeters', 'Position', [2 2 16 7], 'Color', 'w');
    if exist('theme', 'file')
        theme(fig, 'light');                % Force the light theme (R2025a+)
    end
    ax = gca;
    hold on
    box on
    grid on
    ax.FontSize = 11;
    ax.TickLabelInterpreter = 'latex';
    for m = 1:numel(t_report)
        n = find(t >= t_report(m) - Dt/2, 1);
        plot(x, F.(report{b,1})(:,n), ['k' styles{m}], 'LineWidth', 1.4, ...
            'DisplayName', sprintf('$t = %g$', round(t(n), 6)));
    end
    ax.XLim = [-10 10];
    ax.YLim = [-0.05 1.05];
    xlabel('$x$', 'Interpreter', 'latex');
    ylabel('$f$', 'Interpreter', 'latex', 'rotation', 0);
    lgd = legend('Interpreter', 'latex', 'Location', 'northoutside', 'Orientation', 'horizontal');
    % Explicit colours so the figure looks the same whatever the MATLAB theme
    fig.Color = 'w';
    ax.Color = 'w';
    ax.XColor = 'k';
    ax.YColor = 'k';
    ax.GridColor = 'k';
    lgd.Color = 'w';
    lgd.TextColor = 'k';
    lgd.EdgeColor = 'k';
    exportgraphics(fig, fullfile(outdir, [report{b,2} '.pdf']), 'ContentType', 'vector', 'BackgroundColor', 'white');
    exportgraphics(fig, fullfile(outdir, [report{b,2} '.png']), 'Resolution', 300, 'BackgroundColor', 'white');
end

%% Local functions
function f = simulate(f0, U, alpha, Dx, Dt, Nt, BC)
    Nx = numel(f0);
    f = zeros(Nx, Nt);
    f(:,1) = f0;
    for n = 1:Nt-1

        % Inner points (from i = 2 to i = Nx-1), Eq. (10)
        for i = 2:Nx-1
            f(i,n+1) = f(i,n) - U*Dt*(f(i+1,n) - f(i-1,n))/(2*Dx) ...
                     + alpha*Dt*(f(i+1,n) - 2*f(i,n) + f(i-1,n))/Dx^2;
        end

        % Points at boundary (at i = 1 and i = Nx)
        switch BC
            case 'Dirichlet'
            % Dirichlet Boundary Conditions, Eq. (3)
                f(1,n+1) = 0.0;
                f(Nx,n+1) = 0.0;

            case 'Neumann'
            % Neumann Boundary Conditions: Eq. (10) with the ghost nodes
            % of Eq. (11), f(x_0) = f(x_2) and f(x_Nx+1) = f(x_Nx-1)
                f(1,n+1) = f(1,n) + 2*alpha*Dt*(f(2,n) - f(1,n))/Dx^2;
                f(Nx,n+1) = f(Nx,n) + 2*alpha*Dt*(f(Nx-1,n) - f(Nx,n))/Dx^2;

            case 'Periodic'
            % Periodic Boundary Conditions: Eq. (10) with the ghost nodes
            % of Eq. (12), f(x_0) = f(x_Nx-1) and f(x_Nx+1) = f(x_2)
                for j = [1 Nx]
                    f(j,n+1) = f(j,n) - U*Dt*(f(2,n) - f(Nx-1,n))/(2*Dx) ...
                             + alpha*Dt*(f(2,n) - 2*f(j,n) + f(Nx-1,n))/Dx^2;
                end

            otherwise
                error('Unknown boundary condition: %s', BC);
        end
    end
end
