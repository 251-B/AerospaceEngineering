%% =========================================================================
%  MECHANICS APPLIED TO AEROSPACE ENGINEERING (UC3M)
%  LABORATORY 1: PARTICLE CONNECTED TO A SPOOL
%  Authors: Group LA - S1, S2, S3 (Provisional Team)
%
%  Automated master script to integrate the equations of motion for all 
%  5 study cases using ode45 and custom event function stopfun.
%  Generates publication-quality figures conforming to department standards.
% =========================================================================

clc;
clear;
close all;

%% 1. GLOBAL GRAPHICS ROOT CONFIGURATION (Department Style Standard)
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');
set(groot, 'defaultLineLineWidth', 1.8);
set(groot, 'defaultAxesFontSize', 12);
set(groot, 'defaultAxesLineWidth', 1.0);
set(groot, 'defaultAxesXGrid', 'on');
set(groot, 'defaultAxesYGrid', 'on');
set(groot, 'defaultLegendBox', 'off');

% Directory for figure export
figsDir = fullfile(pwd, 'figs');
if ~exist(figsDir, 'dir')
    mkdir(figsDir);
end

%% 2. PHYSICAL PARAMETERS
g    = 9.81;    % Gravity acceleration [m/s^2]
m    = 0.1;     % Particle mass [kg]
a    = 0.20;    % Spool cylinder radius [m]
phi0 = 0.0;     % Initial angle of tangency point B [rad]
xi0  = 1.0;     % Initial unspooled string length [m]

% 5 Study Cases: [CaseNum, omega (rad/s), vx0 (m/s), t_max (s)]
case_data = [
    1,  0.1,   0.0, 55.0;
    2,  0.0,  -1.0, 20.0;
    3,  0.0, -10.0,  1.0;
    4,  0.0,   4.0,  3.0;
    5,  0.1,   1.0, 40.0
];

num_cases = size(case_data, 1);
results = cell(num_cases, 1);

fprintf('=========================================================================\n');
fprintf('   MECHANICS APPLIED TO AEROSPACE ENGINEERING - LAB 1 SIMULATION RUNNER  \n');
fprintf('=========================================================================\n');
fprintf('%-6s | %-12s | %-12s | %-12s | %-25s\n', 'Case', 'omega [rad/s]', 'vx(0) [m/s]', 'Stop Time [s]', 'Termination Reason');
fprintf('-------------------------------------------------------------------------\n');

%% 3. NUMERICAL INTEGRATION OF THE 5 CASES
for k = 1:num_cases
    cNum   = case_data(k, 1);
    omega  = case_data(k, 2);
    vx0    = case_data(k, 3);
    t_span = [0, case_data(k, 4)];

    % At t=0, phi=0: vx0 = xi0 * phi_dot0 => phi_dot0 = vx0 / xi0
    phi_dot0 = vx0 / xi0;
    X0 = [phi0; phi_dot0];

    % Solver options with event detection
    opts = odeset('Events', @(t, X) stopfun(t, X, g, m, a, omega, xi0), ...
                  'RelTol', 1e-7, 'AbsTol', 1e-9, 'MaxStep', 0.02);

    % Numerical integration with ode45
    [tSol, XSol, te, ye, ie] = ode45(@(t, X) diffeq(t, X, g, a, omega, xi0), t_span, X0, opts);

    % State variables extraction
    phi     = XSol(:, 1);
    phi_dot = XSol(:, 2);

    % Unspooled string length: xi(t) = xi0 + a*(phi - omega*t)
    xi = xi0 + a * (phi - omega * tSol);

    % Tangency point B coordinates
    xB = a * cos(phi);
    yB = a * sin(phi);

    % Particle P coordinates: r_P = r_B + xi * [sin(phi); -cos(phi)]
    xP = xB + xi .* sin(phi);
    yP = yB - xi .* cos(phi);

    % Particle velocity components
    % v_P = -a*omega*u + xi*phi_dot*n
    % u = [sin(phi); -cos(phi)], n = [cos(phi); sin(phi)]
    vxP = -a * omega * sin(phi) + xi .* phi_dot .* cos(phi);
    vyP =  a * omega * cos(phi) + xi .* phi_dot .* sin(phi);
    vNormSq = vxP.^2 + vyP.^2;

    % String tension: T = m * (xi * phi_dot^2 + g * cos(phi))
    T = m * (xi .* (phi_dot.^2) + g * cos(phi));

    % Mechanical energy: E = Kinetic + Potential (datum at y = 0)
    E_kin = 0.5 * m * vNormSq;
    E_pot = m * g * yP;
    E_tot = E_kin + E_pot;

    % Determine termination reason
    term_reason = 'Completed max time';
    if ~isempty(ie)
        if ie(end) == 1
            term_reason = sprintf('Hit Spool (xi=0) @ phi=%.2f rad', ye(end,1));
        elseif ie(end) == 2
            term_reason = sprintf('Lost Tension (T=0) @ phi=%.2f rad', ye(end,1));
        end
    end

    fprintf('Case %d | %12.2f | %12.2f | %12.4f | %-25s\n', cNum, omega, vx0, tSol(end), term_reason);

    % Store results in structure
    res.cNum        = cNum;
    res.omega       = omega;
    res.vx0         = vx0;
    res.t           = tSol;
    res.phi         = phi;
    res.phi_dot     = phi_dot;
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

%% 4. PLOTTING PUBLICATION-QUALITY FIGURES

colors = {'#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'};
styles = {'-', '--', '-.', ':', '-'};

% -------------------------------------------------------------------------
% Figure 1: Angular position phi(t)
% -------------------------------------------------------------------------
hFig1 = figure('Name', 'Fig1_Phi_Evolution', 'Units', 'pixels', 'Position', [100, 100, 750, 500]);
hold on;
for k = 1:num_cases
    plot(results{k}.t, results{k}.phi, 'LineWidth', 2.0, 'Color', colors{k}, ...
         'DisplayName', sprintf('Case %d ($\\omega=%.1f, v_{x0}=%d$)', results{k}.cNum, results{k}.omega, results{k}.vx0));
end
xlabel('Time $t$ [s]');
ylabel('Tangency Angle $\phi$ [rad]');
title('Evolution of Spool Tangency Angle $\phi(t)$');
legend('Location', 'best');
xlim([0, 45]);
grid on;
saveas(hFig1, fullfile(figsDir, 'fig1_phi_evolution.png'));
saveas(hFig1, fullfile(figsDir, 'fig1_phi_evolution.eps'), 'epsc');

% -------------------------------------------------------------------------
% Figure 2: Unspooled String Length xi(t)
% -------------------------------------------------------------------------
hFig2 = figure('Name', 'Fig2_Xi_Evolution', 'Units', 'pixels', 'Position', [120, 120, 750, 500]);
hold on;
for k = 1:num_cases
    plot(results{k}.t, results{k}.xi, 'LineWidth', 2.0, 'Color', colors{k}, ...
         'DisplayName', sprintf('Case %d', results{k}.cNum));
end
yline(0, 'k--', 'LineWidth', 1.2, 'DisplayName', 'Spool Boundary ($\xi = 0$)');
xlabel('Time $t$ [s]');
ylabel('Unspooled String Length $\xi$ [m]');
title('Evolution of Unspooled String Length $\xi(t)$');
legend('Location', 'best');
ylim([-0.05, 1.2]);
xlim([0, 45]);
grid on;
saveas(hFig2, fullfile(figsDir, 'fig2_xi_evolution.png'));
saveas(hFig2, fullfile(figsDir, 'fig2_xi_evolution.eps'), 'epsc');

% -------------------------------------------------------------------------
% Figure 3: String Tension T(t)
% -------------------------------------------------------------------------
hFig3 = figure('Name', 'Fig3_Tension_Evolution', 'Units', 'pixels', 'Position', [140, 140, 750, 500]);
hold on;
for k = [1, 2, 4, 5] % Case 3 omitted here to prevent scaling compression due to singularity
    plot(results{k}.t, results{k}.T, 'LineWidth', 2.0, 'Color', colors{k}, ...
         'DisplayName', sprintf('Case %d', results{k}.cNum));
end
yline(0, 'r--', 'LineWidth', 1.5, 'DisplayName', 'Tension Threshold ($T = 0$)');
xlabel('Time $t$ [s]');
ylabel('String Tension $T$ [N]');
title('String Tension Evolution $T(t)$ (Cases 1, 2, 4, 5)');
legend('Location', 'best');
xlim([0, 25]);
ylim([-0.2, 5.0]);
grid on;
saveas(hFig3, fullfile(figsDir, 'fig3_tension_evolution.png'));
saveas(hFig3, fullfile(figsDir, 'fig3_tension_evolution.eps'), 'epsc');

% -------------------------------------------------------------------------
% Figure 4: Trajectories in Oxy Plane (5 Subplots with Spool Circle)
% -------------------------------------------------------------------------
hFig4 = figure('Name', 'Fig4_Trajectories_Oxy', 'Units', 'pixels', 'Position', [160, 160, 1100, 700]);
th_circ = linspace(0, 2*pi, 200);
x_spool = a * cos(th_circ);
y_spool = a * sin(th_circ);

for k = 1:num_cases
    subplot(2, 3, k);
    hold on;
    % Plot Spool
    fill(x_spool, y_spool, [0.85, 0.85, 0.85], 'EdgeColor', 'k', 'LineWidth', 1.5, 'DisplayName', 'Spool');
    % Plot Trajectory
    plot(results{k}.xP, results{k}.yP, 'LineWidth', 2.0, 'Color', colors{k}, 'DisplayName', 'Particle $P$');
    % Plot Initial Position
    plot(results{k}.xP(1), results{k}.yP(1), 'go', 'MarkerFaceColor', 'g', 'MarkerSize', 6, 'DisplayName', 'Initial Point');
    % Plot Final Position
    plot(results{k}.xP(end), results{k}.yP(end), 'rs', 'MarkerFaceColor', 'r', 'MarkerSize', 6, 'DisplayName', 'Final Point');
    
    xlabel('$x$ [m]');
    ylabel('$y$ [m]');
    title(sprintf('Case %d: $\\omega=%.1f$ rad/s, $v_{x0}=%d$ m/s', results{k}.cNum, results{k}.omega, results{k}.vx0));
    axis equal;
    grid on;
    if k == 1
        legend('Location', 'northeast', 'FontSize', 9);
    end
end
saveas(hFig4, fullfile(figsDir, 'fig4_trajectories_Oxy.png'));
saveas(hFig4, fullfile(figsDir, 'fig4_trajectories_Oxy.eps'), 'epsc');

% -------------------------------------------------------------------------
% Figure 5: Total Mechanical Energy Conservation E(t)
% -------------------------------------------------------------------------
hFig5 = figure('Name', 'Fig5_Mechanical_Energy', 'Units', 'pixels', 'Position', [180, 180, 850, 550]);
hold on;
for k = 1:num_cases
    plot(results{k}.t, results{k}.E_tot, 'LineWidth', 2.0, 'Color', colors{k}, ...
         'DisplayName', sprintf('Case %d ($\\omega=%.1f$ rad/s)', results{k}.cNum, results{k}.omega));
end
xlabel('Time $t$ [s]');
ylabel('Total Mechanical Energy $E$ [J]');
title('Mechanical Energy $E(t) = E_k + E_p$ Verification');
legend('Location', 'best');
xlim([0, 35]);
grid on;
saveas(hFig5, fullfile(figsDir, 'fig5_mechanical_energy.png'));
saveas(hFig5, fullfile(figsDir, 'fig5_mechanical_energy.eps'), 'epsc');

% -------------------------------------------------------------------------
% Figure 6: Case 4 Ballistic Extension (Question 11 Demonstration)
% -------------------------------------------------------------------------
hFig6 = figure('Name', 'Fig6_Case4_Ballistic', 'Units', 'pixels', 'Position', [200, 200, 800, 550]);
hold on;
% Taut string stage
plot(results{4}.xP, results{4}.yP, 'Color', '#d62728', 'LineWidth', 2.2, 'DisplayName', 'Stage 1: Taut String ($T > 0$)');
% Ballistic stage continuation
t_slack = results{4}.t(end);
r_slack = [results{4}.xP(end); results{4}.yP(end)];
v_slack = [-a*results{4}.omega*sin(results{4}.phi(end)) + results{4}.xi(end)*results{4}.phi_dot(end)*cos(results{4}.phi(end));
            a*results{4}.omega*cos(results{4}.phi(end)) + results{4}.xi(end)*results{4}.phi_dot(end)*sin(results{4}.phi(end))];
[t_ball, x_ball, y_ball] = simulate_case4_ballistic(t_slack, r_slack, v_slack, g, 0.45);
plot(x_ball, y_ball, 'b--', 'LineWidth', 2.2, 'DisplayName', 'Stage 2: Free Parabolic Flight ($T = 0$)');
% Marker at detachment
plot(r_slack(1), r_slack(2), 'kp', 'MarkerFaceColor', 'y', 'MarkerSize', 10, 'DisplayName', 'Tension Loss ($T = 0$)');
fill(x_spool, y_spool, [0.85, 0.85, 0.85], 'EdgeColor', 'k', 'LineWidth', 1.5, 'DisplayName', 'Spool');
xlabel('$x$ [m]');
ylabel('$y$ [m]');
title('Case 4: Transition to Ballistic Parabolic Flight upon Slackening');
legend('Location', 'best');
axis equal;
grid on;
saveas(hFig6, fullfile(figsDir, 'fig6_case4_ballistic.png'));
saveas(hFig6, fullfile(figsDir, 'fig6_case4_ballistic.eps'), 'epsc');

% -------------------------------------------------------------------------
% Figure 7: Case 3 Singularity Close-Up (Question 10 Demonstration)
% -------------------------------------------------------------------------
hFig7 = figure('Name', 'Fig7_Case3_Singularity', 'Units', 'pixels', 'Position', [220, 220, 800, 500]);
yyaxis left;
plot(results{3}.t, results{3}.xi, 'b-', 'LineWidth', 2.0);
ylabel('Unspooled Length $\xi$ [m]');
ylim([0, 1.05]);

yyaxis right;
plot(results{3}.t, abs(results{3}.phi_dot), 'r-', 'LineWidth', 2.0);
ylabel('Angular Speed $|\dot{\phi}|$ [rad/s]');
set(gca, 'YScale', 'log');

xlabel('Time $t$ [s]');
title('Case 3: Collision Singularity Dynamics ($\xi \to 0 \rightarrow |\dot{\phi}| \to \infty$)');
grid on;
saveas(hFig7, fullfile(figsDir, 'fig7_case3_singularity.png'));
saveas(hFig7, fullfile(figsDir, 'fig7_case3_singularity.eps'), 'epsc');

fprintf('All figures generated and saved successfully to: %s\n', figsDir);
