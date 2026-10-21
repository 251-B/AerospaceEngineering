%% Lab 2 - Particle on oscillating loop
% Mechanics Applied to Aerospace Engineering (UC3M)
% Group LA: Alvarez Iglesias, Gonzalez Rodriguez, Hernandez Bejarano
clear; clc; close all;

% default style of the plots (Script 6 of the Laboratory Guidelines, with a larger font
% so that the labels can be read when the figures are scaled down in the report)
set(groot, 'defaultLegendFontSize', 14);
set(groot, 'defaultTextFontSize', 15);
set(groot, 'defaultAxesFontSize', 15);
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

%% Figure 2 of the report: angle, reaction forces and inertia forces
figure('Position', [50 50 1000 900])
subplot(3,2,1)
plot(t, phi, 'b'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(a) Angle, $t \in [0, 3T]$')

subplot(3,2,2)
plot(t, phi, 'b'); grid on
xlim([0 10])
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(b) Angle, first 10 s')

subplot(3,2,3)
plot(t, Nr, 'b'); grid on
xlim([0 10])
xlabel('$t$ (s)'); ylabel('$N_r$ (N)'); title('(c) Reaction along $\mathbf{e}_r$, first 10 s')

subplot(3,2,4)
plot(t, Nz, 'b'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('$N_z$ (N)'); title('(d) Reaction along $\mathbf{k}$')

subplot(3,2,5)
plot(t, Fcf, 'b', t, Feul, 'r--'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('force (N)'); title('(e) Centrifugal and Euler forces')
ylim([-0.1 0.3])
legend('centrifugal ($\mathbf{i}$)', 'Euler ($\mathbf{k}$)', 'Location', 'north', 'Orientation', 'horizontal')

subplot(3,2,6)
plot(t, Fcor, 'b'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('force (N)'); title('(f) Coriolis force ($\mathbf{k}$)')
saveas(gcf, 'Fig_2.png')

%% Figure 3 of the report: energies
% Ek and Ep repeat the same shape in every oscillation of phi, so they are shown in the first 10 s
figure('Position', [50 50 1000 700])
subplot(2,1,1)
plot(t, Ek, 'b', t, Ep, 'r--'); grid on
xlim([0 10])
xlabel('$t$ (s)'); ylabel('energy (J)'); title('(a) Kinetic and potential energy, first 10 s')
legend('$E_k$', '$E_p$', 'Location', 'eastoutside')

subplot(2,1,2)
plot(t, E - E(1), 'b', t, W, 'r--'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('energy (J)'); title('(b) Mechanical energy and work of the wire, $t \in [0, 3T]$')
legend('$E - E_0$', '$W = \int -\Omega x N_z\, dt$', 'Location', 'eastoutside')
saveas(gcf, 'Fig_3.png')

%% Figure 4 of the report: trajectory of P in the fixed frame
s  = linspace(0, 2*pi, 200);
xw = R*(1 + cos(s));   % wire in the rotating frame
yw = R*sin(s);

figure('Position', [50 50 1100 500])
subplot(1,2,1)
plot3(x1, z1, y1, 'b'); hold on
plot3(xw, 0*s, yw, 'k--')                                    % wire at t = 0
plot3([0 0], [0 0], [-1.2*R 1.2*R], 'k-.')                   % axis of rotation
plot3(x1(1), z1(1), y1(1), 'ko', 'MarkerFaceColor', 'k')     % start
axis equal; grid on; view(35, 20)
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); zlabel('$y_1$ (m)')
title('(a) Trajectory of P')
legend('trajectory of P', 'wire at $t = 0$', 'axis $Oy_1$', '$t = 0$', 'Location', 'southoutside', 'Orientation', 'horizontal', 'NumColumns', 2)

subplot(1,2,2)
plot(x1, z1, 'b'); hold on
plot(x1(1), z1(1), 'ko', 'MarkerFaceColor', 'k')
axis equal; grid on
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); title('(b) View from above')
saveas(gcf, 'Fig_4.png')

%% Figure 5 of the report: phase portrait for A = 0
figure('Position', [50 50 1100 520])
subplot(1,3,[1 2])
hold on
for i = 1:3
    for j = 1:3
        plot(phi7{i,j}, dphi7{i,j}, [colors{i} styles{j}])
        names{3*(i-1)+j} = ['$\varphi_0 = ' phinames{i} '$, $\dot\varphi_0 = ' num2str(dphi0v(j)) '$'];
    end
end
pp = linspace(-3*pi/2, 3*pi, 1000);
sp = sqrt(2*g/R*(1 - sin(pp)));
plot([pp NaN pp], [sp NaN -sp], 'k-.')          % separatrix (both branches)
plot(-pi/2, 0, 'ko', 'MarkerFaceColor', 'k')    % stable equilibrium
plot(pi/2, 0, 'ko')                             % unstable equilibrium
grid on
xlim([-3*pi/2 3*pi])
xlabel('$\varphi$ (rad)'); ylabel('$\dot\varphi$ (rad/s)'); title('(a) Phase portrait ($A = 0$)')
legend([names {'separatrix', 'stable equilibrium', 'unstable equilibrium'}], 'Location', 'eastoutside', 'FontSize', 12)

subplot(1,3,3)
plot(tv{1}, phiv{1}, 'b', tv{2}, phiv{2}, 'r--'); hold on
plot([0 tend7], [pi/2 pi/2], 'k:')
grid on
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(b) $\varphi_0 = \pi/4$, near $\dot\varphi_c$')
legend('$0.99\,\dot\varphi_c$', '$1.01\,\dot\varphi_c$', '$\varphi = \pi/2$', 'Location', 'northwest')
saveas(gcf, 'Fig_5.png')

%% Figure 6 of the report: linearized vs full equation
figure('Position', [50 50 1000 450])
% the error oscillates fast and touches zero, so the largest error reached up to each time
% (envelope) is drawn as a thick line on top of the error itself (thin line)
colors8 = {'b', 'r', 'm'};
subplot(1,2,1)
for k = 1:3
    emax = err{k};
    for i = 2:numel(emax)
        emax(i) = max(emax(i-1), err{k}(i));
    end
    semilogy(t8, err{k} + eps, colors8{k}, 'LineWidth', 0.3); hold on
    he(k) = semilogy(t8, emax, colors8{k}, 'LineWidth', 2);
end
grid on
ylim([1e-2 1e2])
xlabel('$t$ (s)'); ylabel('error (\%)'); title('(a) Error of the linearized equation')
legend(he, '$\omega = \sqrt{g/R}$', '$\omega = \frac{1}{2}\sqrt{g/R}$', '$\omega = \frac{1}{4}\sqrt{g/R}$', 'Location', 'southoutside', 'Orientation', 'horizontal')

subplot(1,2,2)
plot(t8, dfull{2}, 'b', t8, dlin{2}, 'r--'); grid on
xlabel('$t$ (s)'); ylabel('$\delta$ (rad)'); title('(b) $\omega = \frac{1}{2}\sqrt{g/R}$ (resonance)')
legend('full equation', 'linearized equation', 'Location', 'northwest')
saveas(gcf, 'Fig_6.png')

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
