%% Lab 2 - Particle on oscillating loop
% Mechanics Applied to Aerospace Engineering (UC3M)
% Group LA: Alvarez Iglesias, Gonzalez Rodriguez, Hernandez Bejarano
clear; clc; close all;

% default style of the plots (Script 6 of the Laboratory Guidelines). The figures are made
% with the size they have in the report (17 cm wide) and saved at 300 dpi, so the 10 pt
% labels appear at 10 pt in the report and stay sharp
set(groot, 'defaultLegendFontSize', 9);
set(groot, 'defaultTextFontSize', 10);
set(groot, 'defaultAxesFontSize', 10);
set(groot, 'defaultFigurePaperPositionMode', 'auto');
set(groot, 'defaultAxesLineWidth', 1);
set(groot, 'defaultAxesXMinorTick', 'on');
set(groot, 'defaultAxesYMinorTick', 'on');
set(groot, 'defaultLegendBox', 'off');
set(groot, 'defaultLineLineWidth', 1);
set(groot, 'defaultLineMarkerSize', 5);
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');

%% Data of the problem
g     = 9.81;      % gravity (m/s^2)
m     = 1;         % mass of the particle (kg)
R     = 1;         % radius of the wire (m)
A     = pi;        % amplitude of the rotation angle of the loop (rad)
w     = 0.1;       % frequency of the loop oscillation (rad/s)
phi0  = 0;         % initial angle (rad)
dphi0 = 0;         % initial angular rate (rad/s)
Tper  = 2*pi/w;    % period of the rotating reference system (s)

options = odeset('RelTol', 1e-8, 'AbsTol', 1e-10);

%% Items 5 and 6: oscillating loop, t = [0, 3T]
% state X = [phi; dphi]
[t, stateSol] = ode45(@(t,X) diffeq(t, X, g, w, R, A), linspace(0, 3*Tper, 10000), [phi0; dphi0], options);
phi  = stateSol(:,1);
dphi = stateSol(:,2);

Om    = A*w*sin(w*t);       % angular rate of the loop
Omdot = A*w^2*cos(w*t);     % angular acceleration of the loop
x     = R*(1 + cos(phi));   % distance of P to the axis of rotation
y     = R*sin(phi);         % height of P

% inertia forces in the rotating frame (centrifugal along i, Euler and Coriolis along k)
Fcf  = m*Om.^2.*x;
Feul = m*Omdot.*x;
Fcor = -2*m*Om*R.*dphi.*sin(phi);

% reaction of the wire (Nr along e_r, Nz along k)
Nr = -m*R*dphi.^2 + m*g*sin(phi) - Fcf.*cos(phi);
Nz = -(Feul + Fcor);

% energies, with the absolute velocity v = v_rel + Omega x r
Ek = 0.5*m*(R^2*dphi.^2 + Om.^2.*x.^2);
Ep = m*g*y;
E  = Ek + Ep;

% work done by the wire, W = integral of P = -Omega*x*Nz (trapezoidal rule)
P = -Om.*x.*Nz;
W = [0; cumsum(0.5*(P(1:end-1) + P(2:end)).*diff(t))];

% position of P in the fixed frame Ox1y1z1
theta = A*(1 - cos(w*t));   % angle turned by the loop
x1 = x.*cos(theta);
y1 = y;
z1 = -x.*sin(theta);

% checks
Xdot0 = diffeq(0, [phi0; dphi0], g, w, R, A);
fprintf('Item 5: ddphi(0) = %.4f rad/s^2 (expected -g/R = %.4f)\n', Xdot0(2), -g/R);
fprintf('Item 5: phi in [%.4f, %.4f] rad\n', min(phi), max(phi));
fprintf('Item 5: Nr in [%.3f, %.3f] N (-3mg = %.3f N), Nz in [%.3f, %.3f] N\n', min(Nr), max(Nr), -3*m*g, min(Nz), max(Nz));
fprintf('Item 5: max centrifugal %.4f N, Euler in [%.4f, %.4f] N, Coriolis in [%.3f, %.3f] N\n', max(Fcf), min(Feul), max(Feul), min(Fcor), max(Fcor));
fprintf('Item 5: Ek max %.3f J, Ep in [%.3f, %.3f] J, E in [%.4f, %.4f] J, E(3T) - E(0) = %.4f J\n', max(Ek), min(Ep), max(Ep), min(E), max(E), E(end) - E(1));
fprintf('Item 5: max |E - E0 - W| = %.2e J\n', max(abs(E - E(1) - W)));
ip = find(dphi(1:end-1) > 0 & dphi(2:end) <= 0);   % instants where dphi changes from + to -
fprintf('Item 5: period of the oscillation of phi = %.3f s (%d oscillations in 3T)\n', mean(diff(t(ip))), numel(ip));
[~, stateFine] = ode45(@(t,X) diffeq(t, X, g, w, R, A), linspace(0, 3*Tper, 10000), [phi0; dphi0], ...
                       odeset('RelTol', 1e-11, 'AbsTol', 1e-12));
fprintf('Item 5: max change of phi with tighter tolerances = %.2e rad\n', max(abs(stateFine(:,1) - phi)));
fprintf('Item 6: max |sqrt(x1^2 + z1^2) - x| = %.2e m\n', max(abs(sqrt(x1.^2 + z1.^2) - x)));

%% Item 7: fixed loop (A = 0), nine initial conditions
phi0v    = [0 pi/4 pi/2];
dphi0v   = [0 1.5 3];
phinames = {'0', '\pi/4', '\pi/2'};
colors   = {'b', 'r', 'm'};
styles   = {'-', '--', ':'};
tend7    = 4;   % longer than the longest period of the closed orbits (3.4 s)

for i = 1:3
    for j = 1:3
        [t7{i,j}, S7] = ode45(@(t,X) diffeq(t, X, g, w, R, 0), linspace(0, tend7, 2000), [phi0v(i); dphi0v(j)], options);
        phi7{i,j}  = S7(:,1);
        dphi7{i,j} = S7(:,2);

        % analytical criterion: phi increases steadily if dphi0 > dcrit
        dcrit = sqrt(2*g/R*(1 - sin(phi0v(i))));
        if dphi0v(j) > dcrit
            predicted = 'increases steadily';
        elseif dphi0v(j) == dcrit
            predicted = 'stays at the top (unstable equilibrium)';
        else
            predicted = 'oscillates';
        end
        if max(phi7{i,j}) > pi
            observed = 'goes over the top';
        else
            observed = 'does not go over the top';
        end
        E7 = 0.5*m*R^2*dphi7{i,j}.^2 + m*g*R*sin(phi7{i,j});
        fprintf('Item 7: phi0 = %.3f, dphi0 = %.1f, critical = %.3f -> predicted: %s; numerical: %s; max |E - E0|/(mgR) = %.1e\n', ...
                phi0v(i), dphi0v(j), dcrit, predicted, observed, max(abs(E7 - E7(1)))/(m*g*R));
    end
end

% validation of the threshold: 1% below and 1% above the critical rate for phi0 = pi/4
dcrit = sqrt(2*g/R*(1 - sin(pi/4)));
fv = [0.99 1.01];
for k = 1:2
    [tv{k}, Sv] = ode45(@(t,X) diffeq(t, X, g, w, R, 0), linspace(0, tend7, 2000), [pi/4; fv(k)*dcrit], options);
    phiv{k} = Sv(:,1);
    fprintf('Item 7: phi0 = pi/4, dphi0 = %.2f x critical -> max phi = %.3f rad\n', fv(k), max(phiv{k}));
end

%% Item 8: linearized equation, A^2 << g/(R w^2)
Rs  = 0.01;                  % radius of the wire (m)
As  = 0.1;                   % amplitude (rad)
wn  = sqrt(g/Rs);            % natural frequency of small oscillations (rad/s)
ws  = wn*[1 1/2 1/4];        % frequencies of the loop (rad/s)
t8  = linspace(0, 10, 4000)';
% initial conditions (not given in the statement): P at rest at the bottom, delta(0) = 0, ddelta(0) = 0

for k = 1:3
    % full equation (phi = delta - pi/2) and linearized equation
    [~, Sfull] = ode45(@(t,X) diffeq(t, X, g, ws(k), Rs, As), t8, [-pi/2; 0], options);
    [~, Slin]  = ode45(@(t,X) diffeqlin(t, X, g, ws(k), Rs, As), t8, [0; 0], options);
    dfull{k} = Sfull(:,1) + pi/2;
    dlin{k}  = Slin(:,1);

    % percentage error, divided by the amplitude of delta (delta crosses zero)
    err{k} = 100*abs(dlin{k} - dfull{k})/max(abs(dfull{k}));

    % closed-form solution of the linearized equation, to check the integration
    F0 = As^2*ws(k)^2/2;
    if k == 2   % resonance, 2w = wn
        dexact = F0/wn^2*(1 - cos(wn*t8)) - F0/(2*wn)*t8.*sin(wn*t8);
    else
        dexact = F0/wn^2 - F0*cos(2*ws(k)*t8)/(wn^2 - 4*ws(k)^2) ...
                 + (F0/(wn^2 - 4*ws(k)^2) - F0/wn^2)*cos(wn*t8);
    end
    i5 = find(t8 >= 5, 1);
    fprintf('Item 8: w = %.3f rad/s: max|delta| = %.4f rad, error at 5 s = %.2f %%, max error = %.2f %%, max |delta_lin - closed form| = %.1e rad\n', ...
            ws(k), max(abs(dfull{k})), err{k}(i5), max(err{k}), max(abs(dlin{k} - dexact)));
end

%% Common settings of the figures
% colours (checked for colour-blind readers), and a light tone of each one for the bands
cBlue   = [0.043 0.361 0.678];
cRed    = [0.820 0.271 0.047];
cPurple = [0.416 0.239 0.604];
cBand   = [0.780 0.855 0.930];
cGrey   = [0.55 0.55 0.55];

% over [0, 3T] there are 79 swings, too many to draw one by one. For those plots each swing
% is reduced to its largest and smallest value (see swingrange at the end of the file), and
% the time axis is marked in units of T: at T/2, T, 3T/2... the plane is at rest
iswing = [1; ip; numel(t)];        % limits of the swings (maxima of phi)
Tticks = 0:Tper/2:3*Tper;
Tnames = {'0', '$T/2$', '$T$', '$3T/2$', '$2T$', '$5T/2$', '$3T$'};
Tlabel = '$t$ ($T = 62.83$ s)';
phiticks = [-pi -pi/2 0];
phinames = {'$-\pi$', '$-\pi/2$', '$0$'};

%% Figure 2 of the report: angle, reaction forces and inertia forces
figure('Units', 'centimeters', 'Position', [2 2 17 12])
tiledlayout(3, 2, 'TileSpacing', 'compact', 'Padding', 'compact')

% (a) angle over the whole interval: largest and smallest angle of each swing
nexttile
[ts, ymax, ymin] = swingrange(t, phi, iswing);
fill([ts; flipud(ts)], [ymax; flipud(ymin)], cBand, 'EdgeColor', 'none'); hold on
plot(ts, ymax, 'Color', cBlue, 'LineWidth', 1.4); plot(ts, ymin, 'Color', cBlue, 'LineWidth', 1.4)
grid on; xlim([0 3*Tper]); ylim([-3.6 0.5])
xticks(Tticks); xticklabels(Tnames); set(gca, 'XMinorTick', 'off'); yticks(phiticks); yticklabels(phinames); set(gca, 'YMinorTick', 'off')
xlabel(Tlabel); ylabel('$\varphi$ (rad)'); title('(a) Limits of each swing, $t \in [0, 3T]$')

% (b) angle in the first 10 s
nexttile
plot(t, phi, 'Color', cBlue, 'LineWidth', 1.4); grid on
xlim([0 10]); ylim([-3.6 0.5])
yticks(phiticks); yticklabels(phinames); set(gca, 'YMinorTick', 'off')
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(b) Angle, first 10 s')

% (c) radial reaction in the first 10 s
nexttile
plot(t, Nr, 'Color', cBlue, 'LineWidth', 1.4); grid on
xlim([0 10]); ylim([-32 2])
xlabel('$t$ (s)'); ylabel('$N_r$ (N)'); title('(c) Reaction along $\mathbf{e}_r$, first 10 s')

% (d) normal reaction over the whole interval: largest and smallest value of each swing
nexttile
[ts, ymax, ymin] = swingrange(t, Nz, iswing);
fill([ts; flipud(ts)], [ymax; flipud(ymin)], cBand, 'EdgeColor', 'none'); hold on
plot(ts, ymax, 'Color', cBlue, 'LineWidth', 1.4); plot(ts, ymin, 'Color', cBlue, 'LineWidth', 1.4)
grid on; xlim([0 3*Tper]); ylim([-3.5 3.5])
xticks(Tticks); xticklabels(Tnames); set(gca, 'XMinorTick', 'off')
xlabel(Tlabel); ylabel('$N_z$ (N)'); title('(d) Limits of $N_z$ in each swing, $t \in [0, 3T]$')

% (e) normal reaction and Coriolis force around t = T/4: they mirror each other
nexttile
plot(t, Nz, 'Color', cBlue, 'LineWidth', 1.4); hold on
plot(t, Fcor, '--', 'Color', cRed, 'LineWidth', 1.4); grid on
xlim([12 20]); ylim([-3.5 4.8])
xlabel('$t$ (s)'); ylabel('force (N)'); title('(e) $N_z$ and Coriolis force, around $t = T/4$')
legend('$N_z$', '$F_{Cor}$', 'Location', 'north', 'Orientation', 'horizontal')

% (f) the three inertia forces differ by two orders of magnitude: logarithmic scale
nexttile
[ts, ymax] = swingrange(t, abs(Fcor), iswing);
semilogy(ts, ymax, '-', 'Color', cRed, 'LineWidth', 1.4); hold on
[ts, ymax] = swingrange(t, abs(Fcf), iswing);
semilogy(ts, ymax, '--', 'Color', cBlue, 'LineWidth', 1.4)
[ts, ymax] = swingrange(t, abs(Feul), iswing);
semilogy(ts, ymax, '-.', 'Color', cPurple, 'LineWidth', 1.4); grid on
xlim([0 3*Tper]); ylim([1e-3 60]); yticks(10.^(-3:1)); set(gca, 'YMinorGrid', 'off')
xticks(Tticks); xticklabels(Tnames); set(gca, 'XMinorTick', 'off')
xlabel(Tlabel); ylabel('largest force (N)'); title('(f) Inertia forces, largest value in each swing')
lg = legend('Coriolis', 'centrifugal', 'Euler', 'Location', 'north', 'Orientation', 'horizontal');
set(lg, 'ItemTokenSize', [15 18])   % short line samples, so the legend fits inside the plot
exportgraphics(gcf, 'Fig_2.png', 'Resolution', 300)   % 300 dpi, white margins cropped

%% Figure 3 of the report: energies
figure('Units', 'centimeters', 'Position', [2 2 17 8.2])
tiledlayout(2, 2, 'TileSpacing', 'compact', 'Padding', 'compact')

% (a) Ek and Ep repeat the same shape in every swing, so the first 10 s are enough
nexttile
plot(t, Ek, 'Color', cBlue, 'LineWidth', 1.4); hold on
plot(t, Ep, '--', 'Color', cRed, 'LineWidth', 1.4); grid on
xlim([0 10]); ylim([-11 15])
xlabel('$t$ (s)'); ylabel('energy (J)'); title('(a) $E_k$ and $E_p$, first 10 s')
legend('$E_k$', '$E_p$', 'Location', 'north', 'Orientation', 'horizontal')

% (b) mechanical energy over the whole interval: limits of each swing
nexttile
[ts, ymax, ymin] = swingrange(t, E - E(1), iswing);
fill([ts; flipud(ts)], [ymax; flipud(ymin)], cBand, 'EdgeColor', 'none'); hold on
plot(ts, ymax, 'Color', cBlue, 'LineWidth', 1.4); plot(ts, ymin, 'Color', cBlue, 'LineWidth', 1.4)
grid on; xlim([0 3*Tper]); ylim([-0.15 0.4])
xticks(Tticks); xticklabels(Tnames); set(gca, 'XMinorTick', 'off')
xlabel(Tlabel); ylabel('$E - E_0$ (J)'); title('(b) Limits of $E - E_0$ in each swing, $t \in [0, 3T]$')

% (c) energy and work in the first half period: the points of W fall on the line of E
nexttile
ik = find(t <= Tper/2);
plot(t(ik), E(ik) - E(1), 'Color', cBlue, 'LineWidth', 1.4); hold on
plot(t(ik(1:9:end)), W(ik(1:9:end)), 'o', 'Color', cRed, 'MarkerSize', 2.2, 'MarkerFaceColor', cRed); grid on
xlim([0 Tper/2]); ylim([-0.15 0.45])
xlabel('$t$ (s)'); ylabel('energy (J)'); title('(c) $E - E_0$ and work of the wire, $t \in [0, T/2]$')
legend('$E - E_0$', '$W$', 'Location', 'north', 'Orientation', 'horizontal')

% (d) difference between the two, in its own (logarithmic) scale
nexttile
[ts, ymax] = swingrange(t, abs(E - E(1) - W), iswing);
semilogy(ts, ymax, 'Color', cBlue, 'LineWidth', 1.4); grid on
xlim([0 3*Tper]); ylim([1e-6 1e-2]); yticks(10.^(-6:-2)); set(gca, 'YMinorGrid', 'off')
xticks(Tticks); xticklabels(Tnames); set(gca, 'XMinorTick', 'off')
xlabel(Tlabel); ylabel('$|E - E_0 - W|$ (J)'); title('(d) Largest difference in each swing')
exportgraphics(gcf, 'Fig_3.png', 'Resolution', 300)

%% Figure 4 of the report: trajectory of P in the fixed frame
s  = linspace(0, 2*pi, 200);
xw = R*(1 + cos(s));   % wire in the rotating frame
yw = R*sin(s);
ik = find(t <= Tper/2);     % first half period: the plane makes one turn

figure('Units', 'centimeters', 'Position', [2 2 17 8.2])
tiledlayout(1, 2, 'TileSpacing', 'compact', 'Padding', 'compact')

nexttile
h1 = plot3(x1(ik), z1(ik), y1(ik), 'Color', cBlue, 'LineWidth', 1.2); hold on
h2 = plot3(xw, 0*s, yw, 'k--', 'LineWidth', 1.2);                   % wire at t = 0
h3 = plot3([0 0], [0 0], [-1.3*R 1.3*R], 'k-.');                    % axis of rotation
plot3(x1(1), z1(1), y1(1), 'ko', 'MarkerFaceColor', 'k', 'MarkerSize', 6)   % start
axis equal; grid on; view(35, 25)
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); zlabel('$y_1$ (m)'); title('(a) Path of P seen from the ground')
legend([h1 h2 h3], '$t \in [0, T/2]$', 'wire at $t = 0$', 'axis', 'Location', 'northwest')

nexttile
h0 = plot(x1, z1, 'Color', cBand); hold on
h1 = plot(x1(ik), z1(ik), 'Color', cBlue, 'LineWidth', 1.2);
plot(2*R*cos(s), 2*R*sin(s), ':', 'Color', cGrey)                   % reach of P, x = 2R
plot(x1(1), z1(1), 'ko', 'MarkerFaceColor', 'k', 'MarkerSize', 6)
axis equal; grid on; xlim([-2.3 2.3]); ylim([-2.3 2.3])
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); title('(b) View from above')
legend([h1 h0], '$t \in [0, T/2]$', '$t \in [0, 3T]$', 'Location', 'eastoutside')
exportgraphics(gcf, 'Fig_4.png', 'Resolution', 300)

%% Figure 5 of the report: phase portrait for A = 0
% each case gets its number at its starting point; the colour says what the bead does
figure('Units', 'centimeters', 'Position', [2 2 17 10])
tiledlayout(2, 3, 'TileSpacing', 'compact', 'Padding', 'compact')
pp = linspace(-3*pi/2, 5*pi/2, 1000);
sp = sqrt(2*g/R*(1 - sin(pp)));

for panel = 1:2
    if panel == 1
        nexttile(1, [2 2])
    else
        nexttile(3)
    end
    hold on
    hs = plot([pp NaN pp], [sp NaN -sp], 'k-.', 'LineWidth', 1.4);            % separatrix
    for i = 1:3
        for j = 1:3
            n = 3*(i-1) + j;
            if n <= 5
                ho = plot(phi7{i,j}, dphi7{i,j}, 'Color', cBlue, 'LineWidth', 1.2);
            elseif n ~= 7
                hr = plot(phi7{i,j}, dphi7{i,j}, 'Color', cRed, 'LineWidth', 1.2);
            end
        end
    end
    for i = 1:3
        for j = 1:3
            text(phi0v(i), dphi0v(j), num2str(3*(i-1) + j), 'FontSize', 8, 'HorizontalAlignment', 'center', ...
                 'BackgroundColor', 'w', 'EdgeColor', 'k', 'Margin', 1, 'Clipping', 'on')
        end
    end
    grid on
    set(gca, 'XMinorTick', 'off')
    if panel == 1
        plot([-pi/2 3*pi/2], [0 0], 'ko', 'MarkerFaceColor', 'k', 'MarkerSize', 6)   % stable equilibria
        xlim([-3*pi/2 5*pi/2]); ylim([-8 8])
        xticks(-3*pi/2:pi/2:5*pi/2)
        xticklabels({'$-3\pi/2$', '$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$', '$5\pi/2$'})
        title('(a) Phase portrait ($A = 0$), start of each case numbered')
        legend([ho hr hs], 'oscillates', 'goes over the top', 'separatrix', 'Location', 'south', 'Orientation', 'horizontal')
    else
        xlim([0.5 2.7]); ylim([-0.2 3.6])
        xticks([pi/4 pi/2 3*pi/4]); xticklabels({'$\pi/4$', '$\pi/2$', '$3\pi/4$'})
        title('(b) Zoom on the top')
    end
    xlabel('$\varphi$ (rad)'); ylabel('$\dot\varphi$ (rad/s)')
end

nexttile(6)
plot(tv{1}, phiv{1}, 'Color', cBlue, 'LineWidth', 1.4); hold on
plot(tv{2}, phiv{2}, '--', 'Color', cRed, 'LineWidth', 1.4)
plot([0 tend7], [pi/2 pi/2], 'k:'); grid on
ylim([-5 10])
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(c) $\varphi_0 = \pi/4$, near $\dot\varphi_c$')
legend('$0.99\,\dot\varphi_c$', '$1.01\,\dot\varphi_c$', 'top', 'Location', 'northwest')
exportgraphics(gcf, 'Fig_5.png', 'Resolution', 300)

%% Figure 6 of the report: linearized vs full equation
figure('Units', 'centimeters', 'Position', [2 2 17 7.9])
tiledlayout(2, 2, 'TileSpacing', 'compact', 'Padding', 'compact')

% (a) the error oscillates fast and touches zero, so each natural period (2*pi/wn = 0.2 s)
% is reduced to its largest error, in logarithmic scale
nexttile(1, [1 2])
nw = ceil(2*pi/wn/(t8(2) - t8(1)));
iw = (1:nw:numel(t8))';
[ts, ymax] = swingrange(t8, err{1}, iw);
semilogy(ts, ymax, 'Color', cBlue, 'LineWidth', 1.4); hold on
[ts, ymax] = swingrange(t8, err{2}, iw);
semilogy(ts, ymax, '--', 'Color', cRed, 'LineWidth', 1.4)
[ts, ymax] = swingrange(t8, err{3}, iw);
semilogy(ts, ymax, '-.', 'Color', cPurple, 'LineWidth', 1.4); grid on
xlim([0 10]); ylim([1e-2 1e2]); yticks(10.^(-2:2)); set(gca, 'YMinorGrid', 'off')
xlabel('$t$ (s)'); ylabel('error (\%)'); title('(a) Percentage error of the linearized equation, largest value in each natural period')
legend('$\omega = \omega_n$', '$\omega = \omega_n/2$', '$\omega = \omega_n/4$', 'Location', 'south', 'Orientation', 'horizontal')

% (b) and (c) the two solutions in the last second: five oscillations can be followed by eye
for k = 1:2
    nexttile
    plot(t8, dfull{k}, 'Color', cBlue, 'LineWidth', 1.4); hold on
    plot(t8, dlin{k}, '--', 'Color', cRed, 'LineWidth', 1.4); grid on
    xlim([9 10])
    xlabel('$t$ (s)'); ylabel('$\delta$ (rad)')
    if k == 1
        title('(b) $\omega = \omega_n$: phase lag')
        ylim([-0.006 0.022])
    else
        title('(c) $\omega = \omega_n/2$: resonance')
        ylim([-0.25 0.42])
    end
    legend('full', 'linearized', 'Location', 'north', 'Orientation', 'horizontal')
end
exportgraphics(gcf, 'Fig_6.png', 'Resolution', 300)

%% Animation of the motion in the fixed frame (video saved as trajectory_P.avi)
% only the first period T is animated, because the motion repeats in the next two (Figure 4b of the report).
% one frame every 6 points of the solution: about 560 frames in T, that is about
% 20 frames for each oscillation of phi (2.4 s), so the motion is not undersampled
video = VideoWriter('trajectory_P.avi', 'Motion JPEG AVI');
video.FrameRate = 30;
open(video)

figure('Position', [50 50 700 600], 'Color', 'w')
plot3([0 0], [0 0], [-1.2*R 1.2*R], 'k-.'); hold on                 % axis of rotation
hw = plot3(xw, 0*s, yw, 'k', 'LineWidth', 1.5);                     % wire
ht = plot3(x1(1), z1(1), y1(1), 'b');                               % trail of P
hp = plot3(x1(1), z1(1), y1(1), 'ro', 'MarkerFaceColor', 'r', 'MarkerSize', 8);   % particle
axis equal; grid on; view(35, 20)
xlim([-2.2*R 2.2*R]); ylim([-2.2*R 2.2*R]); zlim([-1.2*R 1.2*R])
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); zlabel('$y_1$ (m)')
set(gca, 'FontSize', 14)   % larger labels in the video
% all the frames of a video must have the same size. getframe copies the window from the
% screen, and its size can change with the screen settings, so each frame is printed instead
% to an image of fixed size: 7 x 6 inches at 80 dpi = 560 x 480 pixels
set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 7 6]);

for k = 1:6:find(t <= Tper, 1, 'last')
    % wire turned by theta(t): rotation about the vertical axis
    set(hw, 'XData', xw*cos(theta(k)), 'YData', -xw*sin(theta(k)), 'ZData', yw)
    % trail from t = 0 to the current time, and the particle
    set(ht, 'XData', x1(1:k), 'YData', z1(1:k), 'ZData', y1(1:k))
    set(hp, 'XData', x1(k), 'YData', z1(k), 'ZData', y1(k))
    title(['$t = ' num2str(t(k), '%.1f') '$ s, $\theta = ' num2str(theta(k), '%.2f') '$ rad'])
    frame = print(gcf, '-RGBImage', '-r80');   % image of the figure (480 x 560 x 3)
    writeVideo(video, frame);
end
close(video)
fprintf('Animation saved in trajectory_P.avi\n');

%% Functions
function Xdot = diffeq(t, X, g, w, R, A)
    phi  = X(1);
    dphi = X(2);
    Om   = A*w*sin(w*t);                                   % angular rate of the loop
    ddphi = -g/R*cos(phi) - Om^2*(1 + cos(phi))*sin(phi);  % equation of motion
    Xdot = [dphi; ddphi];
end

function Xdot = diffeqlin(t, X, g, w, R, A)
    delta  = X(1);
    ddelta = X(2);
    Om = A*w*sin(w*t);
    Xdot = [ddelta; -g/R*delta + Om^2];                    % linearized equation
end

function [ts, ymax, ymin] = swingrange(t, y, limits)
    % largest and smallest value of y between each pair of limits (one swing), at its mid time
    n = numel(limits) - 1;
    ts = zeros(n, 1); ymax = ts; ymin = ts;
    for k = 1:n
        idx = limits(k):limits(k+1);
        ts(k)   = 0.5*(t(idx(1)) + t(idx(end)));
        ymax(k) = max(y(idx));
        ymin(k) = min(y(idx));
    end
end
