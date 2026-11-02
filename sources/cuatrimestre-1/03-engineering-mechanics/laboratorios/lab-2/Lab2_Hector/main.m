%% Lab 2 - Particle on oscillating loop
% Mechanics Applied to Aerospace Engineering (UC3M)
% Group LA: Álvarez Iglesias, González Rodríguez, Hernández Bejarano
clear; clc; close all;

% plot style (Script 6 of the guidelines)
set(groot, 'defaultLegendFontSize', 12);
set(groot, 'defaultTextFontSize', 12);
set(groot, 'defaultAxesFontSize', 12);
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
A     = pi;        % amplitude of the loop rotation (rad)
w     = 0.1;       % frequency of the loop (rad/s)
phi0  = 0;         % initial angle (rad)
dphi0 = 0;         % initial angular rate (rad/s)
Tper  = 2*pi/w;    % period of the loop (s)

options = odeset('RelTol', 1e-8, 'AbsTol', 1e-10);

%% Items 5 and 6: oscillating loop, t = [0, 3T]
% state X = [phi; dphi]
tspan = linspace(0, 3*Tper, 10000);
[t, stateSol] = ode45(@(t,X) diffeq(t, X, g, w, R, A), tspan, [phi0; dphi0], options);
phi  = stateSol(:,1);
dphi = stateSol(:,2);

Om    = A*w*sin(w*t);       % angular velocity of the loop
Omdot = A*w^2*cos(w*t);     % angular acceleration of the loop
x     = R*(1 + cos(phi));   % distance to the axis
y     = R*sin(phi);         % height of P

% inertia forces
Fcf  = m*Om.^2.*x;                     % centrifugal, along i
Feul = m*Omdot.*x;                     % Euler, along k
Fcor = -2*m*Om*R.*dphi.*sin(phi);      % Coriolis, along k

% reaction of the wire
Nr = -m*R*dphi.^2 + m*g*sin(phi) - Fcf.*cos(phi);
Nz = -(Feul + Fcor);

% energies
Ek = 0.5*m*(R^2*dphi.^2 + Om.^2.*x.^2);
Ep = m*g*y;
E  = Ek + Ep;

% position of P in the fixed frame
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

% period of the swing: times where dphi goes from + to -
n = 0;
for i = 1:length(t)-1
    if dphi(i) > 0 && dphi(i+1) <= 0
        n = n + 1;
        tp(n) = t(i);
    end
end
fprintf('Item 5: period of the oscillation of phi = %.3f s (%d oscillations in 3T)\n', (tp(n) - tp(1))/(n - 1), n);

% same run with tighter tolerances
options2 = odeset('RelTol', 1e-11, 'AbsTol', 1e-12);
[~, stateFine] = ode45(@(t,X) diffeq(t, X, g, w, R, A), tspan, [phi0; dphi0], options2);
fprintf('Item 5: max change of phi with tighter tolerances = %.2e rad\n', max(abs(stateFine(:,1) - phi)));
fprintf('Item 6: max |sqrt(x1^2 + z1^2) - x| = %.2e m\n', max(abs(sqrt(x1.^2 + z1.^2) - x)));

%% Item 7: fixed loop (A = 0), nine initial conditions
phi0v    = [0 pi/4 pi/2];
dphi0v   = [0 1.5 3];
phinames = {'0', '\pi/4', '\pi/2'};
tend7    = 4;   % longest closed curve is 3.36 s

for i = 1:3
    for j = 1:3
        [~, S7] = ode45(@(t,X) diffeq(t, X, g, w, R, 0), linspace(0, tend7, 2000), [phi0v(i); dphi0v(j)], options);
        phi7{i,j}  = S7(:,1);
        dphi7{i,j} = S7(:,2);

        % critical rate from the energy
        dcrit = sqrt(2*g/R*(1 - sin(phi0v(i))));
        if dphi0v(j) > dcrit
            predicted = 'increases steadily';
        elseif dphi0v(j) == dcrit
            predicted = 'stays at the top (unstable equilibrium)';
        else
            predicted = 'oscillates';
        end
        if max(phi7{i,j}) > pi/2 + 1e-3   % top of the loop
            observed = 'goes over the top';
        else
            observed = 'does not go over the top';
        end
        E7 = 0.5*m*R^2*dphi7{i,j}.^2 + m*g*R*sin(phi7{i,j});
        fprintf('Item 7: phi0 = %.3f, dphi0 = %.1f, critical = %.3f -> predicted: %s; numerical: %s; max |E - E0|/(mgR) = %.1e\n', ...
                phi0v(i), dphi0v(j), dcrit, predicted, observed, max(abs(E7 - E7(1)))/(m*g*R));

        % period of the closed curves: 30 s run, times where dphi goes from + to -
        if dphi0v(j) < dcrit
            [tl, Sl] = ode45(@(t,X) diffeq(t, X, g, w, R, 0), linspace(0, 30, 30000), [phi0v(i); dphi0v(j)], options);
            n = 0;
            for k = 1:length(tl)-1
                if Sl(k,2) > 0 && Sl(k+1,2) <= 0
                    n = n + 1;
                    tp7(n) = tl(k);
                end
            end
            fprintf('Item 7: phi0 = %.3f, dphi0 = %.1f -> period %.3f s\n', phi0v(i), dphi0v(j), (tp7(n) - tp7(1))/(n - 1));
        end
    end
end

%% Item 8: linearized equation, A^2 << g/(R w^2)
Rs  = 0.01;                  % radius of the wire (m)
As  = 0.1;                   % amplitude (rad)
wn  = sqrt(g/Rs);            % natural frequency (rad/s)
ws  = wn*[1 1/2 1/4];        % frequencies of the loop (rad/s)
t8  = linspace(0, 10, 4000)';
% initial conditions not given: P at rest at the bottom, delta(0) = 0, deltadot(0) = 0

for k = 1:3
    % full equation (phi = delta - pi/2) and linearized one
    [~, Sfull] = ode45(@(t,X) diffeq(t, X, g, ws(k), Rs, As), t8, [-pi/2; 0], options);
    [~, Slin]  = ode45(@(t,X) diffeqlin(t, X, g, ws(k), Rs, As), t8, [0; 0], options);
    dfull{k} = Sfull(:,1) + pi/2;
    dlin{k}  = Slin(:,1);

    % percentage error over the amplitude (delta crosses zero)
    err{k} = 100*abs(dlin{k} - dfull{k})/max(abs(dfull{k}));

    % exact solution of the linearized equation
    F0 = As^2*ws(k)^2/2;
    if k == 2   % resonance, 2w = wn
        dexact = F0/wn^2*(1 - cos(wn*t8)) - F0/(2*wn)*t8.*sin(wn*t8);
    else
        dexact = F0/wn^2 - F0*cos(2*ws(k)*t8)/(wn^2 - 4*ws(k)^2) ...
                 + (F0/(wn^2 - 4*ws(k)^2) - F0/wn^2)*cos(wn*t8);
    end
    i5 = find(t8 >= 5, 1);
    fprintf('Item 8: w = %.3f rad/s: max|delta| = %.5f rad, error at 5 s = %.2f %%, max error = %.2f %%, max |delta_lin - exact| = %.1e rad\n', ...
            ws(k), max(abs(dfull{k})), err{k}(i5), max(err{k}), max(abs(dlin{k} - dexact)));
end

%% Figure 2: angle and reaction forces
% one panel per magnitude, saved at the report width (17 cm)
% 79 swings in 3T look like a solid band, so phi and Nr also get a zoom of the first 10 s
figure('Units', 'centimeters', 'Position', [2 2 17 11.2])
subplot(3,2,1)
plot(t, phi, 'b'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(a) Angle')

subplot(3,2,2)
plot(t, phi, 'b'); grid on
xlim([0 10])
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(b) Angle, first 10 s')

subplot(3,2,3)
plot(t, Nr, 'b'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('$N_r$ (N)'); title('(c) Reaction along $\mathbf{e}_r$')

subplot(3,2,4)
plot(t, Nr, 'b'); grid on
xlim([0 10])
xlabel('$t$ (s)'); ylabel('$N_r$ (N)'); title('(d) Reaction along $\mathbf{e}_r$, first 10 s')

subplot(3,2,[5 6])
plot(t, Nz, 'b'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('$N_z$ (N)'); title('(e) Reaction along $\mathbf{k}$')
exportgraphics(gcf, 'Fig_2.png', 'Resolution', 600)

%% Figure 3: inertia forces
figure('Units', 'centimeters', 'Position', [2 2 17 11.2])
subplot(3,1,1)
plot(t, Fcf, 'b'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('$F_{cf}$ (N)'); title('(a) Centrifugal force (along $\mathbf{i}$)')

subplot(3,1,2)
plot(t, Feul, 'b'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('$F_{Eul}$ (N)'); title('(b) Euler force (along $\mathbf{k}$)')

subplot(3,1,3)
plot(t, Fcor, 'b'); grid on
xlim([0 3*Tper])
xlabel('$t$ (s)'); ylabel('$F_{Cor}$ (N)'); title('(c) Coriolis force (along $\mathbf{k}$)')
exportgraphics(gcf, 'Fig_3.png', 'Resolution', 600)

%% Figure 4: kinetic and potential energy
% full time and zoom of the first 10 s
figure('Units', 'centimeters', 'Position', [2 2 17 6])
subplot(1,2,1)
plot(t, Ek, 'b'); hold on
plot(t, Ep, 'r--'); grid on
xlim([0 3*Tper]); ylim([-12 14])
xlabel('$t$ (s)'); ylabel('energy (J)'); title('(a) $t \in [0, 3T]$')
legend('$E_k$', '$E_p$', 'Location', 'north', 'Orientation', 'horizontal')

subplot(1,2,2)
plot(t, Ek, 'b'); hold on
plot(t, Ep, 'r--'); grid on
xlim([0 10]); ylim([-12 14])
xlabel('$t$ (s)'); ylabel('energy (J)'); title('(b) First 10 s')
exportgraphics(gcf, 'Fig_4.png', 'Resolution', 600)

%% Figure 5: trajectory of P in the fixed frame
s  = linspace(0, 2*pi, 200);
xw = R*(1 + cos(s));   % wire, also used in the video
yw = R*sin(s);

figure('Units', 'centimeters', 'Position', [2 2 17 7.5])
plot3(x1, z1, y1, 'b'); hold on
plot3(xw, 0*s, yw, 'k--', 'LineWidth', 1.5)                % wire at t = 0
plot3([0 0], [0 0], [-1.3*R 1.3*R], 'k-.')                 % axis of rotation
plot3(x1(1), z1(1), y1(1), 'ko', 'MarkerFaceColor', 'k')   % start
axis equal; grid on; view(35, 25)
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); zlabel('$y_1$ (m)')
legend('trajectory of P, $t \in [0, 3T]$', 'wire at $t = 0$', 'axis $Oy_1$', 'start, $t = 0$', 'Location', 'eastoutside')
exportgraphics(gcf, 'Fig_5.png', 'Resolution', 600)

%% Figure 6: phase portrait for A = 0
% colour: phi(0), line style: dphi(0), dot: start
colors7 = {'b', 'r', 'm'};
styles7 = {'-', '--', ':'};
figure('Units', 'centimeters', 'Position', [2 2 17 8.3])
hold on
for i = 1:3
    for j = 1:3
        h7(3*(i-1)+j) = plot(phi7{i,j}, dphi7{i,j}, styles7{j}, 'Color', colors7{i}, 'LineWidth', 1.3);
        plot(phi0v(i), dphi0v(j), 'o', 'Color', colors7{i}, 'MarkerFaceColor', colors7{i})
        names{3*(i-1)+j} = ['$\varphi_0 = ' phinames{i} '$, $\dot\varphi_0 = ' num2str(dphi0v(j)) '$ rad/s'];
    end
end
% limit curve between oscillating and going over the top, Eq. (21)
pp = linspace(-3*pi/2, 5*pi/2, 1000);
sp = sqrt(2*g/R*(1 - sin(pp)));
h7(10) = plot(pp, sp, 'k-.', 'LineWidth', 1.3);
plot(pp, -sp, 'k-.', 'LineWidth', 1.3)
grid on
xlim([-3*pi/2 5*pi/2]); ylim([-8 8])
xlabel('$\varphi$ (rad)'); ylabel('$\dot\varphi$ (rad/s)')
legend(h7, [names {'limit curve'}], 'Location', 'eastoutside', 'FontSize', 10)
exportgraphics(gcf, 'Fig_6.png', 'Resolution', 600)

%% Figure 7: percentage error of the linearized equation
% error from 0.01 % to 30 %, so log axis
figure('Units', 'centimeters', 'Position', [2 2 17 7])
semilogy(t8, err{1} + eps, 'b'); hold on
semilogy(t8, err{2} + eps, 'r--')
semilogy(t8, err{3} + eps, 'm:', 'LineWidth', 1.3); grid on
xlim([0 10]); ylim([1e-3 1e2])
yticks([1e-3 1e-2 1e-1 1 10 100]); set(gca, 'YMinorGrid', 'off')
xlabel('$t$ (s)'); ylabel('error (\%)')
legend('$\omega = \sqrt{g/R}$', '$\omega = \frac{1}{2}\sqrt{g/R}$', '$\omega = \frac{1}{4}\sqrt{g/R}$', 'Location', 'northoutside', 'Orientation', 'horizontal')
exportgraphics(gcf, 'Fig_7.png', 'Resolution', 600)

%% Video of the first period (trajectory_P.avi)
video = VideoWriter('trajectory_P.avi');
video.FrameRate = 30;
open(video)

figure('Position', [50 50 700 600], 'Color', 'w')
for k = 1:6:find(t <= Tper, 1, 'last')   % one frame every 6 points
    clf
    plot3([0 0], [0 0], [-1.2*R 1.2*R], 'k-.'); hold on                      % axis of rotation
    plot3(xw*cos(theta(k)), -xw*sin(theta(k)), yw, 'k', 'LineWidth', 1.5)    % wire turned by theta
    plot3(x1(1:k), z1(1:k), y1(1:k), 'b')                                    % trail of P
    plot3(x1(k), z1(k), y1(k), 'ro', 'MarkerFaceColor', 'r', 'MarkerSize', 8)   % particle
    axis equal; grid on; view(35, 20)
    xlim([-2.2*R 2.2*R]); ylim([-2.2*R 2.2*R]); zlim([-1.2*R 1.2*R])
    xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); zlabel('$y_1$ (m)')
    title(['$t = ' num2str(t(k), '%.1f') '$ s, $\theta = ' num2str(theta(k), '%.2f') '$ rad'])
    frame = getframe(gcf);
    if k == 1
        sz = size(frame.cdata);   % size of the first frame
    end
    if isequal(size(frame.cdata), sz)   % skip a frame of another size
        writeVideo(video, frame);
    end
end
close(video)
fprintf('Animation saved in trajectory_P.avi\n');

%% Functions
function Xdot = diffeq(t, X, g, w, R, A)
    phi  = X(1);
    dphi = X(2);
    Om   = A*w*sin(w*t);                                   % angular velocity of the loop
    ddphi = -g/R*cos(phi) - Om^2*(1 + cos(phi))*sin(phi);  % equation of motion
    Xdot = [dphi; ddphi];
end

function Xdot = diffeqlin(t, X, g, w, R, A)
    delta    = X(1);
    deltadot = X(2);
    Om = A*w*sin(w*t);
    Xdot = [deltadot; -g/R*delta + Om^2];                  % linearized equation
end
