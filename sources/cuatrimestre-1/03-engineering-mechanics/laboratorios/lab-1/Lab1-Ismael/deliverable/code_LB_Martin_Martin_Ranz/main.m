%% Laboratory 1: Particle connected to a spool
% Mechanics Applied to Aerospace Engineering, UC3M
% Ismael Martin Diez, David Martin Garcia, Alejandro Ranz Remartinez
clc
clear
close all

% Format of the plots for overleaf (LaTeX)
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');
set(groot, 'defaultLineLineWidth', 1.5);
set(groot, 'defaultAxesFontSize', 12);

if ~isfolder('figures')
    mkdir('figures')
end

% Data
g = 9.81;          % gravity [m/s^2]
m = 0.1;           % mass [kg]
a = 0.2;           % radius of the spool [m]
phi0 = 0;          % initial angle [rad]
xi0 = 1;           % initial unspooled length [m]

% Study cases
omega_cases = [0.1 0 0 0 0.1];   % [rad/s]
v0_cases = [0 -1 -10 4 1];       % xdotP(0) [m/s]
tf_cases = [100 10 100 100 100]; % final time [s], only 10s in second because it never ends

th = linspace(0, 2*pi, 300);

for k = 1:5
    omega = omega_cases(k);
    phidot0 = v0_cases(k)/xi0; % at phi = 0, xdotP = xi*phidot
    X0 = [phi0; phidot0];

    % Integration (the step is limited so that ode45 does not skip the events)
    options = odeset('Events', @(t, X) stopfun(t, X, g, omega, a, xi0, m), 'RelTol', 1e-8, 'MaxStep', 0.01);
    [t, X, te, Xe, ie] = ode45(@(t, X) diffeq(t, X, g, omega, a, xi0), [0 tf_cases(k)], X0, options);

    phi = X(:, 1);
    phidot = X(:, 2);

    % Formulas of the report
    xi = xi0 - a*(omega*t - phi);
    T = m*xi.*phidot.^2 + m*g*cos(phi);
    x = a*cos(phi) + xi.*sin(phi);
    y = a*sin(phi) - xi.*cos(phi);
    E = 0.5*m*(xi.^2.*phidot.^2 + a^2*omega^2) + m*g*y;

    % Results of the case
    fprintf('\n=== Case %d: omega = %.1f rad/s, xP_dot(0) = %.0f m/s ===\n', k, omega, v0_cases(k));
    fprintf('phidot(0) = xP_dot(0)/xi0 = %.1f rad/s\n', phidot0);
    % Check why does the simulation stop
    if isempty(ie) 
        fprintf('event: none, final time reached\n');
    elseif ie(end) == 1
        fprintf('event: the particle hits the spool (xi = 0)\n');
    else
        fprintf('event: the string loses tension (T = 0)\n');
    end
    %Printing of all the data
    fprintf('t_end = %.5f s\n', t(end));
    fprintf('P(t_end) = (%.5f, %.5f) m\n', x(end), y(end));
    fprintf('E(0) = %.5f J, E(t_end) = %.5f J\n', E(1), E(end));
    fprintf('phi(t_end) = %.5f rad = %.1f deg, xi(t_end) = %.2e m\n', phi(end), phi(end)*180/pi, xi(end));
    fprintf('phi in [%.5f, %.5f] rad\n', min(phi), max(phi));
    fprintf('xi in [%.5f, %.5f] m\n', min(xi), max(xi));
    fprintf('T in [%.4f, %.4f] N, T(0) = %.3f N, T(t_end) = %.3e N\n', min(T), max(T), T(1), T(end));
    fprintf('B(t_end) = (%.5f, %.5f) m\n', a*cos(phi(end)), a*sin(phi(end)));
    fprintf('|v_P(t_end)| = %.4f m/s, phidot(t_end) = %.3e rad/s\n', sqrt((xi(end)*phidot(end))^2 + (a*omega)^2), phidot(end));

    if k == 1
        fprintf('a*omega = %.3f m/s, xi0/(a*omega) = %.1f s, m*g = %.3f N\n', a*omega, xi0/(a*omega), m*g);
        fprintf('max|phi| = %.1e rad, dE/dt = %.5f W, m*g*a*omega = %.5f W\n', max(abs(phi)), (E(end) - E(1))/t(end), m*g*a*omega);
    end
    if k == 3
        fprintf('contact time t_c = %.6f s\n', t(end));
        % Speed at the contact with te spool
        vc = sqrt(2*(E(1)/m - g*y(end)));
        fprintf('v_c from the energy = %.4f m/s, xi*|phidot| at the end = %.4f m/s\n', ...
            vc, xi(end)*abs(phidot(end)));
        fprintf('m*xP_dot(0)^2/xi0 + m*g = %.3f N\n', m*v0_cases(k)^2/xi0 + m*g);
    end
    if k == 4
        fprintf('xi*phidot^2 at t_end = %.3f m/s^2, g*|cos(phi)| at t_end = %.3f m/s^2\n', ...
            xi(end)*phidot(end)^2, g*abs(cos(phi(end))));
        fprintf('pi/2 = %.5f rad (phi_max must be below it)\n', pi/2);
    end
    if k == 5
        % Swings to the right (max of phi) and to the left (min of phi)
        pmax = phi(islocalmax(phi));
        imin = find(islocalmin(phi));
        fprintf('maxima of phi: first = %.4f rad, last = %.4f rad\n', pmax(1), pmax(end));
        fprintf('minima of phi: first = %.4f rad, last = %.4f rad (t = %.2f s, xi = %.4f m)\n', ...
            phi(imin(1)), phi(imin(end)), t(imin(end)), xi(imin(end)));
        fprintf('omega*t_end = %.3f rad, xi0/a = %.1f rad, omega*t_end - phi(t_end) = %.3f rad\n', ...
            omega*t(end), xi0/a, omega*t(end) - phi(end));
        fprintf('contact %.1f s earlier than in case 1 (50 s)\n', xi0/(a*omega) - t(end));
    end

    % Figure of the case
    fig = figure('Position', [100 100 900 480], 'Color', 'w');
    try
        theme(fig, 'light');
    end

    subplot(2, 2, 1)
    yyaxis left
    plot(t, phi)
    ylabel('$\phi$ [rad]')
    if k == 3, ylim([-6 0]), end
    yyaxis right
    plot(t, xi)
    ylabel('$\xi$ [m]')
    xlabel('$t$ [s]')
    title('(a)')
    grid on

    subplot(2, 2, 2)
    plot(t, T, 'k')
    xlabel('$t$ [s]')
    ylabel('$T$ [N]')
    title('(b)')
    if k == 3
        set(gca, 'YScale', 'log')
    elseif k == 5
        ylim([0 4])
    end
    grid on

    subplot(2, 2, 3)
    plot(a*cos(th), a*sin(th), 'r--')
    hold on
    plot(x, y, 'b')
    plot(x(1), y(1), 'ko', 'MarkerFaceColor', 'k')
    plot(x(end), y(end), 'ks', 'MarkerFaceColor', 'k')
    axis equal
    xlabel('$x$ [m]')
    ylabel('$y$ [m]')
    title('(c)')
    grid on

    subplot(2, 2, 4)
    plot(t, E, 'm')
    xlabel('$t$ [s]')
    ylabel('$E$ [J]')
    title('(d)')
    if omega == 0
        ylim([E(1) - 0.5, E(1) + 0.5])
    end
    grid on

    exportgraphics(fig, sprintf('figures/case%d.png', k), 'Resolution', 200)
end

%% Functions
function Xdot = diffeq(t, X, g, omega, a, xi0)
phi = X(1);
phidot = X(2);
xi = xi0 - a*(omega*t - phi);
phiddot = (-g*sin(phi) - a*phidot^2 + 2*a*omega*phidot)/xi;
Xdot = [phidot; phiddot];
end

function [value, isterminal, direction] = stopfun(t, X, g, omega, a, xi0, m)
phi = X(1);
phidot = X(2);
xi = xi0 - a*(omega*t - phi);
T = m*xi*phidot^2 + m*g*cos(phi);
% xi - 1e-6 instead of xi: ode45 cannot reach xi = 0 exactly
value = [xi - 1e-6; T];
isterminal = [1; 1];
direction = [-1; -1];
end
