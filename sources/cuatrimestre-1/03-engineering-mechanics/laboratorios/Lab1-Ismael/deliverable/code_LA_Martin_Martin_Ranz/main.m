%% Laboratory Session 1 - Particle connected to a spool
% Mechanics Applied to Aerospace Engineering - UC3M - 2026/2027 - Group LA
% Ismael Martin Diez, David Martin Garcia, Alejandro Ranz Remartinez
%
% Running this script (no user input required) integrates the five study
% cases, prints the main results in the command window and saves every
% figure of the report, in PDF and PNG, to ./figures.
% diffeq, stopfun and the plotting helpers are local functions at the end
% of this file (as in example1.m).

clc; clear; close all;

%% Plot formatting (Lab guidelines, Script 6; example1.m)
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');
set(groot, 'defaultLineLineWidth', 1.5);
set(groot, 'defaultAxesFontSize', 12);
set(groot, 'defaultTextFontSize', 12);
set(groot, 'defaultLegendFontSize', 11);
set(groot, 'defaultAxesXMinorTick', 'on');
set(groot, 'defaultAxesYMinorTick', 'on');
set(groot, 'defaultLegendBox', 'off');
set(groot, 'defaultAxesBox', 'on');
warning('off', 'MATLAB:print:ContentTypeImageSuggested');

fig_dir = fullfile(fileparts(mfilename('fullpath')), 'figures');
if ~isfolder(fig_dir), mkdir(fig_dir); end

%% Parameters (Lab guidelines, Sec. 1.1)
g    = 9.81;     % gravity                    [m/s^2]
m    = 0.1;      % mass of P                  [kg]
a    = 0.20;     % spool radius               [m]
phi0 = 0;        % initial angle of OB        [rad]
xi0  = 1.0;      % initial unspooled length   [m]

% Study cases: omega [rad/s] and xP_dot(0) [m/s]
omega_c = [0.1,  0.0,   0.0, 0.0, 0.1];
v0_c    = [0.0, -1.0, -10.0, 4.0, 1.0];
% Final time [s]: case 2 has no event (it oscillates forever), so it is
% integrated over about five periods; the other cases stop at an event.
tf_c    = [100,  10,   100, 100, 100];

% Contact tolerance [m]: near the spool phiddot ~ 1/xi and ode45 cannot
% step exactly onto xi = 0, so the contact event is placed at xi = xi_tol.
xi_tol = 1e-6;

%% Integration of the five cases (items 5-8)
S = cell(1, 5);
for k = 1:5
    omega = omega_c(k);
    % At phi0 = 0, v_P = xi0*phidot0 i + a*omega j  ->  phidot0 = xP_dot(0)/xi0
    phidot0 = v0_c(k)/xi0;

    options = odeset('RelTol', 1e-8, 'AbsTol', 1e-8, 'MaxStep', 1e-2, ...
        'Events', @(t,X) stopfun(t, X, g, omega, a, xi0, m, xi_tol));
    [t, X, ~, ~, ie] = ode45(@(t,X) diffeq(t, X, g, omega, a, xi0), ...
        [0 tf_c(k)], [phi0; phidot0], options);

    s = struct();
    s.t      = t;
    s.phi    = X(:,1);
    s.phidot = X(:,2);
    s.xi     = xi0 - a*(omega*t - s.phi);                          % [m]
    s.T      = m*s.xi.*s.phidot.^2 + m*g*cos(s.phi);               % [N]
    s.x      = a*cos(s.phi) + s.xi.*sin(s.phi);                    % [m]
    s.y      = a*sin(s.phi) - s.xi.*cos(s.phi);                    % [m]
    s.xB     = a*cos(s.phi);                                       % [m]
    s.yB     = a*sin(s.phi);                                       % [m]
    s.v      = sqrt((s.xi.*s.phidot).^2 + (a*omega)^2);            % [m/s]
    s.E      = 0.5*m*s.v.^2 + m*g*s.y;                             % [J]
    if isempty(ie)
        s.event = 'none (final time)';
    elseif ie(end) == 1
        s.event = 'spool contact (xi = 0)';
    else
        s.event = 'string slack (T = 0)';
    end
    S{k} = s;
end

%% Results in the command window
fprintf('\nLAB 1 - PARTICLE CONNECTED TO A SPOOL\n');
fprintf('%-5s %6s %6s %10s %10s  %-24s %9s %9s %10s\n', 'Case', 'omega', 'v0', ...
    'E0 [J]', 't_end [s]', 'event', 'x_end [m]', 'y_end [m]', 'E_end [J]');
for k = 1:5
    s = S{k};
    fprintf('%-5d %6.2f %6.1f %10.5f %10.5f  %-24s %9.5f %9.5f %10.5f\n', k, omega_c(k), ...
        v0_c(k), s.E(1), s.t(end), s.event, s.x(end), s.y(end), s.E(end));
end

% Item 10
s = S{3};
fprintf('\nCase 3: P hits the spool at t = %.6f s, phi = %.5f rad, P = (%.5f, %.5f) m,\n', ...
    s.t(end), s.phi(end), s.x(end), s.y(end));
fprintf('        speed |v| = %.4f m/s, |phidot| = %.3e rad/s at xi = %.0e m\n', ...
    s.v(end), abs(s.phidot(end)), s.xi(end));
s = S{4};
fprintf('Case 4: the string goes slack at t = %.5f s, phi = %.5f rad, xi = %.5f m,\n', ...
    s.t(end), s.phi(end), s.xi(end));
fprintf('        P = (%.5f, %.5f) m, B = (%.5f, %.5f) m, max(phi) = %.5f rad\n', ...
    s.x(end), s.y(end), s.xB(end), s.yB(end), max(s.phi));
s = S{5};
fprintf('Case 5: stop condition: %s at t = %.5f s, phi = %.5f rad (min T = %.4f N)\n', ...
    s.event, s.t(end), s.phi(end), min(s.T));

%% Figures 2-6: phi, xi, T and trajectory of each case (items 7-8)
% Tension axis: logarithmic in case 3 (T grows without bound before the
% contact); in case 5 linear and cut at 4 N for the same reason.
T_axis = {'lin', 'lin', 'log', 'lin', [0 4]};
for k = 1:5
    fig = plot_case(S{k}, a, T_axis{k});
    save_figure(fig, fig_dir, sprintf('fig_case%d', k));
end

%% Figure 7: mechanical energy of each case (item 9)
fig = plot_energy(S, omega_c);
save_figure(fig, fig_dir, 'fig_energy');

%% Figure 8: phidot near the end of case 3 (item 10)
s = S{3};
fig = new_figure(8.5, 6.5);
loglog(s.xi, abs(s.phidot), 'b-', 'DisplayName', '$|\dot\phi|$');  hold on;
loglog(s.xi, s.v(end)./s.xi, 'r--', 'DisplayName', '$v_c/\xi$');
xlabel('$\xi$ [m]');  ylabel('$|\dot\phi|$ [rad/s]');
legend('Location', 'northeast');  grid on;  xlim([xi_tol 1]);
set(gca, 'XMinorGrid', 'off', 'YMinorGrid', 'off', 'XTick', 10.^(-6:2:0), 'YTick', 10.^(0:2:6));
save_figure(fig, fig_dir, 'fig_case3_phidot');

fprintf('\nFigures saved to %s\n', fig_dir);

%% ========================================================================
%  Local functions
%  ========================================================================
function Xdot = diffeq(t, X, g, omega, a, xi0)
% dX/dt = f(t,X) with X = [phi; phidot] (item 5).
% xi from the constraint xi = xi0 - a*(omega*t - phi); phiddot from the
% e_r component of Newton's law, which does not contain the tension.
phi    = X(1);
phidot = X(2);
xi      = xi0 - a*(omega*t - phi);
phiddot = (-g*sin(phi) - a*phidot^2 + 2*a*omega*phidot) / xi;
Xdot = [phidot; phiddot];
end

function [value, isterminal, direction] = stopfun(t, X, g, omega, a, xi0, m, xi_tol)
% Stop when P reaches the spool (xi = 0) or the string goes slack (T = 0) (item 6).
phi    = X(1);
phidot = X(2);
xi = xi0 - a*(omega*t - phi);
T  = m*xi*phidot^2 + m*g*cos(phi);
value      = [xi - xi_tol; T];
isterminal = [1; 1];
direction  = [-1; -1];
end

function fig = plot_case(s, a, T_axis)
% (a) phi and xi versus t (separate vertical axes), (b) tension, (c) trajectory.
fig = new_figure(17, 6.2);
tl = tiledlayout(fig, 1, 10, 'TileSpacing', 'compact', 'Padding', 'compact');
c_phi = [0 0.447 0.741];  c_xi = [0.85 0.325 0.098];

ax = nexttile(tl, [1 3]);
yyaxis(ax, 'left');
plot(ax, s.t, s.phi, '-', 'Color', c_phi);
ylabel(ax, '$\phi$ [rad]');  ax.YColor = c_phi;
yyaxis(ax, 'right');
plot(ax, s.t, s.xi, '-', 'Color', c_xi, 'LineWidth', 1.2);
ylabel(ax, '$\xi$ [m]');  ax.YColor = c_xi;
xlabel(ax, '$t$ [s]');  title(ax, '(a)');  grid(ax, 'on');  xlim(ax, [0 s.t(end)]);

ax = nexttile(tl, [1 3]);
if strcmp(T_axis, 'log')
    semilogy(ax, s.t, s.T, 'k-');
    ax.YMinorGrid = 'off';
else
    plot(ax, s.t, s.T, 'k-', 'LineWidth', 1.2);  hold(ax, 'on');
    yline(ax, 0, ':', 'LineWidth', 1);
    if isnumeric(T_axis)
        ylim(ax, T_axis);
    elseif min(s.T) > 0
        ylim(ax, [0, 1.15*max(s.T)]);
    end
end
xlabel(ax, '$t$ [s]');  ylabel(ax, '$T$ [N]');  title(ax, '(b)');
grid(ax, 'on');  xlim(ax, [0 s.t(end)]);

ax = nexttile(tl, [1 4]);
th = linspace(0, 2*pi, 400);
fill(ax, a*cos(th), a*sin(th), [0.88 0.88 0.88], 'EdgeColor', [0.3 0.3 0.3], 'LineWidth', 1);
hold(ax, 'on');
plot(ax, 0, 0, 'k+', 'MarkerSize', 6, 'LineWidth', 1);
plot(ax, s.x, s.y, '-', 'Color', c_phi, 'LineWidth', 1.2);
plot(ax, [s.xB(1) s.x(1)], [s.yB(1) s.y(1)], 'k:', 'LineWidth', 1);
plot(ax, [s.xB(end) s.x(end)], [s.yB(end) s.y(end)], 'k-.', 'LineWidth', 1);
plot(ax, s.x(1), s.y(1), 'ko', 'MarkerFaceColor', 'w', 'MarkerSize', 6);
plot(ax, s.x(end), s.y(end), 'ks', 'MarkerFaceColor', 'k', 'MarkerSize', 6);
plot(ax, s.xB(1), s.yB(1), 'k^', 'MarkerFaceColor', 'w', 'MarkerSize', 5);
axis(ax, 'equal');  grid(ax, 'on');
xlabel(ax, '$x$ [m]');  ylabel(ax, '$y$ [m]');  title(ax, '(c)');
xlim(ax, [min([s.x; -a]) - 0.1, max([s.x; a]) + 0.1]);
ylim(ax, [min([s.y; -a]) - 0.1, max([s.y; a]) + 0.1]);
if numel(ax.XTick) > 4, ax.XTick = ax.XTick(1:2:end); end
end

function fig = plot_energy(S, omega_c)
% Mechanical energy versus time, one panel per case.
fig = new_figure(17, 10);
tl = tiledlayout(fig, 2, 6, 'TileSpacing', 'compact', 'Padding', 'compact');
first_tile = [1 3 5 8 10];        % 3 panels on the first row, 2 centred below
labels = {'(a) Case 1', '(b) Case 2', '(c) Case 3', '(d) Case 4', '(e) Case 5'};
for k = 1:5
    s = S{k};
    ax = nexttile(tl, first_tile(k), [1 2]);
    plot(ax, s.t, s.E, 'b-');
    if omega_c(k) == 0
        ylim(ax, s.E(1) + [-0.05 0.05]);   % E constant: show it on a readable scale
    end
    xlabel(ax, '$t$ [s]');  ylabel(ax, '$E$ [J]');  title(ax, labels{k});
    grid(ax, 'on');  xlim(ax, [0 s.t(end)]);
end
end

function fig = new_figure(w, h)
% w x h cm figure in the light theme (R2025a may default to a dark theme).
fig = figure('Units', 'centimeters', 'Position', [2 2 w h], 'Color', 'w');
try
    theme(fig, 'light');
catch
    % older releases have no themes and are light by default
end
end

function save_figure(fig, fig_dir, name)
exportgraphics(fig, fullfile(fig_dir, [name '.pdf']), 'ContentType', 'vector');
exportgraphics(fig, fullfile(fig_dir, [name '.png']), 'Resolution', 300);
end
