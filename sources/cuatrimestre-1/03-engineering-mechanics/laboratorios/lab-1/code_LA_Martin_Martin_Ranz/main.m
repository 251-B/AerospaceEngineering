%% =========================================================================
%  MECHANICS APPLIED TO AEROSPACE ENGINEERING (UC3M) - COURSE CODE: 251-14165
%  LABORATORY SESSION 1: PARTICLE CONNECTED TO A ROTATING SPOOL
%
%  Authors: Group LA
%    - Ismael Martin Diez
%    - David Martin Garcia
%    - Alejandro Ranz Remartinez
%
%  All-in-one standalone script solving the 5 study cases via ode45 and stopfun.
%  Follows the exact single-file structure of course examples (example1.m & example2.m).
%  Pure light/white theme with high-contrast black text for report figures.
% =========================================================================

clc;
clear;
close all;

%% 1. GLOBAL GRAPHICS ROOT CONFIGURATION (Light / White Mode Standard)
set(groot, 'defaultFigureColor', 'w');
set(groot, 'defaultAxesColor', 'w');
set(groot, 'defaultAxesXColor', 'k');
set(groot, 'defaultAxesYColor', 'k');
set(groot, 'defaultTextColor', 'k');
set(groot, 'defaultAxesGridColor', [0.25, 0.25, 0.25]);
set(groot, 'defaultAxesGridAlpha', 0.25);
set(groot, 'defaultAxesGridLineStyle', ':');
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');
set(groot, 'defaultLineLineWidth', 2.0);
set(groot, 'defaultAxesFontSize', 12);
set(groot, 'defaultAxesLineWidth', 1.0);
set(groot, 'defaultAxesXGrid', 'on');
set(groot, 'defaultAxesYGrid', 'on');
set(groot, 'defaultLegendBox', 'off');

% Directory for figure output
figsDir = fullfile(pwd, 'figs');
if ~exist(figsDir, 'dir')
    mkdir(figsDir);
end

%% 2. PHYSICAL PARAMETERS & STUDY CASES
g    = 9.81;    % Gravity acceleration [m/s^2]
m    = 0.1;     % Particle mass [kg]
a    = 0.20;    % Spool cylinder radius [m]
phi0 = 0.0;     % Initial tangency angle [rad]
xi0  = 1.0;     % Initial unspooled string length [m]

% Matrix of study cases: [CaseNum, omega (rad/s), vx0 (m/s), t_max (s)]
cases_matrix = [
    1,  0.1,   0.0, 55.0;
    2,  0.0,  -1.0, 20.0;
    3,  0.0, -10.0,  1.0;
    4,  0.0,   4.0,  3.0;
    5,  0.1,   1.0, 40.0
];

num_cases = size(cases_matrix, 1);
results = cell(num_cases, 1);

fprintf('=========================================================================\n');
fprintf('   LAB 1: PARTICLE CONNECTED TO A SPOOL - SIMULATION RUNNER (GROUP LA)   \n');
fprintf('=========================================================================\n');
fprintf('%-6s | %-12s | %-12s | %-12s | %-28s\n', 'Case', 'omega [rad/s]', 'vx(0) [m/s]', 'Stop Time [s]', 'Termination Reason');
fprintf('-------------------------------------------------------------------------\n');

%% 3. NUMERICAL INTEGRATION OF ALL CASES
for k = 1:num_cases
    cNum   = cases_matrix(k, 1);
    omega  = cases_matrix(k, 2);
    vx0    = cases_matrix(k, 3);
    t_span = [0, cases_matrix(k, 4)];

    % Initial condition conversion: at t=0, phi=0 => vx(0) = xi0 * phi_dot(0)
    phidot0 = vx0 / xi0;
    X0 = [phi0; phidot0];

    % Solver options with event detection
    options = odeset('Events', @(t, X) stopfun(t, X, g, omega, a, xi0, m), ...
                     'RelTol', 1e-8, 'AbsTol', 1e-9, 'MaxStep', 0.02);

    % Integration with ode45
    [tSol, XSol, te, ye, ie] = ode45(@(t, X) diffeq(t, X, g, omega, a, xi0), t_span, X0, options);

    % Extract variables
    phi    = XSol(:, 1);
    phidot = XSol(:, 2);

    % Unspooled string length: xi(t) = xi0 - a*(omega*t - phi) = xi0 + a*(phi - omega*t)
    xi = xi0 - a * (omega * tSol - phi);

    % Tangency point B coordinates
    xB = a * cos(phi);
    yB = a * sin(phi);

    % Particle P Cartesian coordinates
    xP = a * cos(phi) + xi .* sin(phi);
    yP = a * sin(phi) - xi .* cos(phi);

    % Particle velocity components
    vxP = -a * omega * sin(phi) + xi .* phidot .* cos(phi);
    vyP =  a * omega * cos(phi) + xi .* phidot .* sin(phi);
    vNormSq = vxP.^2 + vyP.^2;

    % String tension: T = m * xi * phidot^2 + m * g * cos(phi)
    T = m * xi .* (phidot.^2) + m * g * cos(phi);

    % Total mechanical energy: E = E_kin + E_pot (datum at y = 0)
    E_kin = 0.5 * m * vNormSq;
    E_pot = m * g * yP;
    E_tot = E_kin + E_pot;

    % Determine termination cause
    term_reason = 'Completed max time';
    if ~isempty(ie)
        if ie(end) == 1
            term_reason = sprintf('Hit Spool (xi=0) @ phi=%.2f rad', ye(end,1));
        elseif ie(end) == 2
            term_reason = sprintf('Lost Tension (T=0) @ phi=%.2f rad', ye(end,1));
        end
    end

    fprintf('Case %d | %12.2f | %12.2f | %12.4f | %-28s\n', cNum, omega, vx0, tSol(end), term_reason);

    % Store in results structure
    res.cNum        = cNum;
    res.omega       = omega;
    res.vx0         = vx0;
    res.t           = tSol;
    res.phi         = phi;
    res.phidot      = phidot;
    res.xi          = xi;
    res.xP          = xP;
    res.yP          = yP;
    res.xB          = xB;
    res.yB          = yB;
    res.T           = T;
    res.E_tot       = E_tot;
    res.term_reason = term_reason;
    res.te          = te;
    res.ye          = ye;
    res.ie          = ie;
    results{k}      = res;
end
fprintf('-------------------------------------------------------------------------\n\n');

%% 4. PUBLICATION-QUALITY PLOTTING (Crisp White Background)
colors = {'#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'};

% -------------------------------------------------------------------------
% Figure 1: Angular position phi(t)
% -------------------------------------------------------------------------
hFig1 = figure('Name', 'fig1_phi_evolution', 'Color', 'w', 'Units', 'pixels', 'Position', [100, 100, 750, 500]);
hold on;
for k = 1:num_cases
    plot(results{k}.t, results{k}.phi, 'LineWidth', 2.0, 'Color', colors{k}, ...
         'DisplayName', sprintf('Case %d ($\\omega=%.1f$ rad/s, $v_{x0}=%d$ m/s)', ...
         results{k}.cNum, results{k}.omega, results{k}.vx0));
end
xlabel('Time $t$ [s]');
ylabel('Tangency Angle $\phi$ [rad]');
title('Evolution of Spool Tangency Angle $\phi(t)$');
legend('Location', 'best', 'TextColor', 'k');
xlim([0, 45]);
grid on;
set(gca, 'Color', 'w', 'XColor', 'k', 'YColor', 'k');
exportgraphics(hFig1, fullfile(figsDir, 'fig1_phi_evolution.png'), 'BackgroundColor', 'white');
exportgraphics(hFig1, fullfile(figsDir, 'fig1_phi_evolution.eps'), 'BackgroundColor', 'white');

% -------------------------------------------------------------------------
% Figure 2: Unspooled String Length xi(t)
% -------------------------------------------------------------------------
hFig2 = figure('Name', 'fig2_xi_evolution', 'Color', 'w', 'Units', 'pixels', 'Position', [120, 120, 750, 500]);
hold on;
for k = 1:num_cases
    plot(results{k}.t, results{k}.xi, 'LineWidth', 2.0, 'Color', colors{k}, ...
         'DisplayName', sprintf('Case %d', results{k}.cNum));
end
yline(0, 'k--', 'LineWidth', 1.2, 'DisplayName', 'Spool Surface ($\xi = 0$)');
xlabel('Time $t$ [s]');
ylabel('Unspooled Length $\xi$ [m]');
title('Evolution of Unspooled String Length $\xi(t)$');
legend('Location', 'best', 'TextColor', 'k');
ylim([-0.05, 1.2]);
xlim([0, 45]);
grid on;
set(gca, 'Color', 'w', 'XColor', 'k', 'YColor', 'k');
exportgraphics(hFig2, fullfile(figsDir, 'fig2_xi_evolution.png'), 'BackgroundColor', 'white');
exportgraphics(hFig2, fullfile(figsDir, 'fig2_xi_evolution.eps'), 'BackgroundColor', 'white');

% -------------------------------------------------------------------------
% Figure 3: String Tension T(t)
% -------------------------------------------------------------------------
hFig3 = figure('Name', 'fig3_tension_evolution', 'Color', 'w', 'Units', 'pixels', 'Position', [140, 140, 750, 500]);
hold on;
for k = [1, 2, 4, 5] % Case 3 omitted here to prevent vertical axis compression
    plot(results{k}.t, results{k}.T, 'LineWidth', 2.0, 'Color', colors{k}, ...
         'DisplayName', sprintf('Case %d', results{k}.cNum));
end
yline(0, 'r--', 'LineWidth', 1.5, 'DisplayName', 'Slackening Threshold ($T = 0$)');
xlabel('Time $t$ [s]');
ylabel('String Tension $T$ [N]');
title('String Tension Evolution $T(t)$ (Cases 1, 2, 4, 5)');
legend('Location', 'best', 'TextColor', 'k');
xlim([0, 25]);
ylim([-0.2, 5.0]);
grid on;
set(gca, 'Color', 'w', 'XColor', 'k', 'YColor', 'k');
exportgraphics(hFig3, fullfile(figsDir, 'fig3_tension_evolution.png'), 'BackgroundColor', 'white');
exportgraphics(hFig3, fullfile(figsDir, 'fig3_tension_evolution.eps'), 'BackgroundColor', 'white');

% -------------------------------------------------------------------------
% Figure 4: Trajectories in the Oxy Plane (5 Subplots with Spool)
% -------------------------------------------------------------------------
hFig4 = figure('Name', 'fig4_trajectories_Oxy', 'Color', 'w', 'Units', 'pixels', 'Position', [160, 160, 1100, 700]);
th_circ = linspace(0, 2*pi, 200);
x_spool = a * cos(th_circ);
y_spool = a * sin(th_circ);

for k = 1:num_cases
    subplot(2, 3, k);
    hold on;
    fill(x_spool, y_spool, [0.90, 0.90, 0.90], 'EdgeColor', 'k', 'LineWidth', 1.5, 'DisplayName', 'Spool');
    plot(results{k}.xP, results{k}.yP, 'LineWidth', 2.0, 'Color', colors{k}, 'DisplayName', 'Trajectory');
    plot(results{k}.xP(1), results{k}.yP(1), 'go', 'MarkerFaceColor', 'g', 'MarkerSize', 6, 'DisplayName', 'Start');
    plot(results{k}.xP(end), results{k}.yP(end), 'rs', 'MarkerFaceColor', 'r', 'MarkerSize', 6, 'DisplayName', 'End');
    
    xlabel('$x$ [m]');
    ylabel('$y$ [m]');
    title(sprintf('Case %d: $\\omega=%.1f$ rad/s, $v_{x0}=%d$ m/s', ...
          results{k}.cNum, results{k}.omega, results{k}.vx0));
    axis equal;
    grid on;
    set(gca, 'Color', 'w', 'XColor', 'k', 'YColor', 'k');
    if k == 1
        legend('Location', 'northeast', 'FontSize', 9, 'TextColor', 'k');
    end
end
exportgraphics(hFig4, fullfile(figsDir, 'fig4_trajectories_Oxy.png'), 'BackgroundColor', 'white');
exportgraphics(hFig4, fullfile(figsDir, 'fig4_trajectories_Oxy.eps'), 'BackgroundColor', 'white');

% -------------------------------------------------------------------------
% Figure 5: Total Mechanical Energy Conservation E(t)
% -------------------------------------------------------------------------
hFig5 = figure('Name', 'fig5_mechanical_energy', 'Color', 'w', 'Units', 'pixels', 'Position', [180, 180, 850, 550]);
hold on;
for k = 1:num_cases
    plot(results{k}.t, results{k}.E_tot, 'LineWidth', 2.0, 'Color', colors{k}, ...
         'DisplayName', sprintf('Case %d ($\\omega=%.1f$ rad/s)', results{k}.cNum, results{k}.omega));
end
xlabel('Time $t$ [s]');
ylabel('Total Mechanical Energy $E$ [J]');
title('Mechanical Energy $E(t) = E_k + E_p$ Verification');
legend('Location', 'best', 'TextColor', 'k');
xlim([0, 35]);
grid on;
set(gca, 'Color', 'w', 'XColor', 'k', 'YColor', 'k');
exportgraphics(hFig5, fullfile(figsDir, 'fig5_mechanical_energy.png'), 'BackgroundColor', 'white');
exportgraphics(hFig5, fullfile(figsDir, 'fig5_mechanical_energy.eps'), 'BackgroundColor', 'white');

% -------------------------------------------------------------------------
% Figure 6: Case 4 Ballistic Extension (Question 11 Demonstration)
% -------------------------------------------------------------------------
hFig6 = figure('Name', 'fig6_case4_ballistic', 'Color', 'w', 'Units', 'pixels', 'Position', [200, 200, 800, 550]);
hold on;
plot(results{4}.xP, results{4}.yP, 'Color', '#d62728', 'LineWidth', 2.2, 'DisplayName', 'Taut Phase ($T > 0$)');

% Ballistic free-flight stage
t_slack = results{4}.t(end);
r_slack = [results{4}.xP(end); results{4}.yP(end)];
v_slack = [-a*results{4}.omega*sin(results{4}.phi(end)) + results{4}.xi(end)*results{4}.phidot(end)*cos(results{4}.phi(end));
            a*results{4}.omega*cos(results{4}.phi(end)) + results{4}.xi(end)*results{4}.phidot(end)*sin(results{4}.phi(end))];
[t_ball, x_ball, y_ball] = simulate_case4_ballistic(t_slack, r_slack, v_slack, g, 0.45);
plot(x_ball, y_ball, 'b--', 'LineWidth', 2.2, 'DisplayName', 'Ballistic Free-Fall ($T = 0$)');
plot(r_slack(1), r_slack(2), 'kp', 'MarkerFaceColor', 'y', 'MarkerSize', 10, 'DisplayName', 'Slackening Point');
fill(x_spool, y_spool, [0.90, 0.90, 0.90], 'EdgeColor', 'k', 'LineWidth', 1.5, 'DisplayName', 'Spool');

xlabel('$x$ [m]');
ylabel('$y$ [m]');
title('Case 4: Transition to Ballistic Parabolic Flight upon Slackening');
legend('Location', 'best', 'TextColor', 'k');
axis equal;
grid on;
set(gca, 'Color', 'w', 'XColor', 'k', 'YColor', 'k');
exportgraphics(hFig6, fullfile(figsDir, 'fig6_case4_ballistic.png'), 'BackgroundColor', 'white');
exportgraphics(hFig6, fullfile(figsDir, 'fig6_case4_ballistic.eps'), 'BackgroundColor', 'white');

% -------------------------------------------------------------------------
% Figure 7: Case 3 Singularity Close-Up (Question 10 Demonstration)
% -------------------------------------------------------------------------
hFig7 = figure('Name', 'fig7_case3_singularity', 'Color', 'w', 'Units', 'pixels', 'Position', [220, 220, 800, 500]);
yyaxis left;
plot(results{3}.t, results{3}.xi, 'b-', 'LineWidth', 2.0);
ylabel('Unspooled Length $\xi$ [m]');
ylim([0, 1.05]);

yyaxis right;
plot(results{3}.t, abs(results{3}.phidot), 'r-', 'LineWidth', 2.0);
ylabel('Angular Speed $|\dot{\phi}|$ [rad/s]');
set(gca, 'YScale', 'log');

xlabel('Time $t$ [s]');
title('Case 3: Collision Singularity Dynamics ($\xi \to 0 \rightarrow |\dot{\phi}| \to \infty$)');
grid on;
set(gca, 'Color', 'w', 'XColor', 'k');
exportgraphics(hFig7, fullfile(figsDir, 'fig7_case3_singularity.png'), 'BackgroundColor', 'white');
exportgraphics(hFig7, fullfile(figsDir, 'fig7_case3_singularity.eps'), 'BackgroundColor', 'white');

fprintf('All figures generated and saved successfully to: %s\n', figsDir);


%% =========================================================================
%% LOCAL FUNCTIONS (Identical format to course examples)
%% =========================================================================

function Xdot = diffeq(t, X, g, omega, a, xi0)
% DIFFEQ State-space equations of motion for the rotating spool problem.
% State vector: X(1) = phi [rad], X(2) = phi_dot [rad/s]
    phi    = X(1);
    phidot = X(2);

    % Unspooled string length from kinematic constraint
    xi = xi0 - a * (omega * t - phi);

    % Numerical safeguard against zero length
    if xi <= 1e-7
        xi = 1e-7;
    end

    % Angular acceleration decoupled from tension via normal projection
    phiddot = (-g * sin(phi) - a * phidot^2 + 2 * a * omega * phidot) / xi;

    Xdot = [phidot; phiddot];
end

function [value, isterminal, direction] = stopfun(t, X, g, omega, a, xi0, m)
% STOPFUN Event function for ODE45 to detect spool collision and slackening.
    phi    = X(1);
    phidot = X(2);

    % Unspooled string length
    xi = xi0 - a * (omega * t - phi);

    % String tension from radial/tangential Newton projection
    T = m * xi * phidot^2 + m * g * cos(phi);

    % Physical contact threshold: 1 mm from the spool cylinder surface.
    % Prevents ode45 step-size collapse at the exact algebraic singularity (xi=0).
    eps_contact = 1e-3;

    value      = [xi - eps_contact; T];
    isterminal = [1; 1];
    direction  = [-1; -1];
end

function [t_ball, x_ball, y_ball] = simulate_case4_ballistic(t0_ball, r0_ball, v0_ball, g, duration)
% SIMULATE_CASE4_BALLISTIC Simulates unconstrained 2D ballistic free-fall
% following tether slackening (T = 0) in Case 4.
    dt = 0.001;
    t_ball = t0_ball : dt : (t0_ball + duration);
    tau = t_ball - t0_ball;

    % Free parabolic motion: x_ddot = 0, y_ddot = -g
    x_ball = r0_ball(1) + v0_ball(1) * tau;
    y_ball = r0_ball(2) + v0_ball(2) * tau - 0.5 * g * tau.^2;
end
