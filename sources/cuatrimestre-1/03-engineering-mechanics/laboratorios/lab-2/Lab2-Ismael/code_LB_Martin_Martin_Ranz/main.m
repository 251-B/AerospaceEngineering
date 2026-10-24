%% Laboratory 2: Particle on oscillating loop
% Mechanics Applied to Aerospace Engineering, UC3M
% Ismael Martin Diez, David Martin Garcia, Alejandro Ranz Remartinez
clc
clear
close all

% Plot formatting
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');
set(groot, 'defaultLineLineWidth', 1.5);
set(groot, 'defaultAxesFontSize', 12);

if ~isfolder('figures')
    mkdir('figures')
end

options = odeset('RelTol', 1e-8, 'MaxStep', 0.01);
g = 9.81;          % gravity [m/s^2]
m = 1;             % mass [kg]

%% Point 5: oscillating loop
A = pi;            % [-]
w = 0.1;           % omega [rad/s]
R = 1;             % radius of the wire [m]
X0 = [0; 0];       % [phi(0); phidot(0)]
Tp = 2*pi/w;       % period of the rotating frame [s]

[t, X] = ode45(@(t, X) diffeq(t, X, g, w, R, A), [0 3*Tp], X0, options);
phi = X(:, 1);
phidot = X(:, 2);

% formulas of the report
Om = A*w*sin(w*t);                 % Omega(t) [rad/s]
Omdot = A*w^2*cos(w*t);            % dOmega/dt [rad/s^2]
rho = R*(1 + cos(phi));            % distance from P to the axis Oy [m]
N1 = -m*R*phidot.^2 + m*g*sin(phi) - m*Om.^2.*rho.*cos(phi);
N2 = 2*m*Om*R.*phidot.*sin(phi) - m*Omdot.*rho;
Fcent = m*Om.^2.*rho;              % along i
Feul = m*Omdot.*rho;               % along k
Fcor = -2*m*Om*R.*phidot.*sin(phi); % along k
Ek = 0.5*m*(R^2*phidot.^2 + Om.^2.*rho.^2);
Ep = m*g*R*sin(phi);
E = Ek + Ep;
P = -Om.*rho.*N2;                  % power of the wire N.v [W]
W = cumtrapz(t, P);                % work of the wire [J]

% swing period from the lowest points of phi
tmin = t(islocalmin(phi));
Tsw = mean(diff(tmin));

fprintf('\n=== Point 5: A = pi, omega = %.1f rad/s, R = %.0f m ===\n', w, R);
fprintf('T = 2*pi/omega = %.2f s, 3T = %.1f s\n', Tp, 3*Tp);
fprintf('max|Omega| = A*omega = %.4f rad/s, max|dOmega/dt| = A*omega^2 = %.4f rad/s^2\n', A*w, A*w^2);
fprintf('(A*omega)^2/(g/R) = %.4f\n', (A*w)^2/(g/R));
Xd0 = diffeq(0, X0, g, w, R, A);
fprintf('phiddot(0) = %.2f rad/s^2 (-g/R = %.2f)\n', Xd0(2), -g/R);
fprintf('phi in [%.4f, %.4f] rad, phidot in [%.3f, %.3f] rad/s\n', min(phi), max(phi), min(phidot), max(phidot));
fprintf('swing period = %.3f s, small-oscillation period 2*pi*sqrt(R/g) = %.3f s\n', Tsw, 2*pi*sqrt(R/g));
fprintf('number of swings in 3T = %.1f\n', 3*Tp/Tsw);
fprintf('N1 in [%.2f, %.2f] N, -3mg = %.2f N\n', min(N1), max(N1), -3*m*g);
fprintf('N2 in [%.3f, %.3f] N\n', min(N2), max(N2));
fprintf('max|F_cent| = %.4f N, 2mA^2omega^2R = %.4f N\n', max(abs(Fcent)), 2*m*(A*w)^2*R);
fprintf('max|F_Euler| = %.4f N, 2mA*omega^2*R = %.4f N\n', max(abs(Feul)), 2*m*A*w^2*R);
fprintf('max|F_Cor| = %.3f N, 2mA*omega*R*max|phidot| = %.3f N\n', max(abs(Fcor)), 2*m*A*w*R*max(abs(phidot)));
fprintf('Ek in [%.3f, %.3f] J, Ep in [%.3f, %.3f] J\n', min(Ek), max(Ek), min(Ep), max(Ep));
fprintf('E(0) = %.4f J, E - E0 in [%.4f, %.4f] J, E(3T) - E0 = %.4f J\n', E(1), min(E - E(1)), max(E - E(1)), E(end) - E(1));
fprintf('max|E - E0 - W| = %.1e J\n', max(abs(E - E(1) - W)));

% 3T window: only the signals that do not collapse into a solid band
fig = figure('Position', [100 100 900 480], 'Color', 'w');
try
    theme(fig, 'light');
end
subplot(2, 2, 1)
plot(t, N2, 'r')
xlabel('$t$ [s]'); ylabel('$N_2$ [N]'); title('(a)')
xlim([0 3*Tp]); grid on
subplot(2, 2, 2)
plot(t, Fcor, 'r')
xlabel('$t$ [s]'); ylabel('$F_{Cor}$ [N]'); title('(b)')
xlim([0 3*Tp]); grid on
subplot(2, 2, 3)
plot(t, Fcent, 'k'); hold on
plot(t, Feul, 'g')
xlabel('$t$ [s]'); ylabel('$F$ [N]'); title('(c)')
legend('$F_{cent}$', '$F_{Euler}$', 'Location', 'northeast')
xlim([0 3*Tp]); grid on
subplot(2, 2, 4)
plot(t, E - E(1), 'k'); hold on
plot(t, W, 'r--')
xlabel('$t$ [s]'); ylabel('[J]'); title('(d)')
legend('$E-E_0$', '$W_N$', 'Location', 'northeast')
xlim([0 3*Tp]); grid on
exportgraphics(fig, 'figures/point5.png', 'Resolution', 200)

% first 10 s: swings, reactions and energies
fig = figure('Position', [100 100 900 480], 'Color', 'w');
try
    theme(fig, 'light');
end
subplot(2, 2, 1)
plot(t, phi, 'b')
xlabel('$t$ [s]'); ylabel('$\varphi$ [rad]'); title('(a)')
xlim([0 10]); grid on
subplot(2, 2, 2)
plot(t, N1, 'b'); hold on
plot(t, N2, 'r')
xlabel('$t$ [s]'); ylabel('$N$ [N]'); title('(b)')
legend('$N_1$', '$N_2$', 'Location', 'southeast')
xlim([0 10]); grid on
subplot(2, 2, 3)
plot(t, Ek, 'm'); hold on
plot(t, Ep, 'c')
plot(t, E, 'k')
xlabel('$t$ [s]'); ylabel('$E$ [J]'); title('(c)')
legend('$E_k$', '$E_p$', '$E$', 'Location', 'southeast', 'NumColumns', 3)
xlim([0 10]); grid on
subplot(2, 2, 4)
plot(t, Fcor, 'r'); hold on
plot(t, Fcent, 'k')
plot(t, Feul, 'g')
xlabel('$t$ [s]'); ylabel('$F$ [N]'); title('(d)')
legend('$F_{Cor}$', '$F_{cent}$', '$F_{Euler}$', 'Location', 'southeast', 'NumColumns', 3)
xlim([0 10]); grid on
exportgraphics(fig, 'figures/point5_zoom.png', 'Resolution', 200)
%% Point 6: trajectory in the fixed frame Ox1y1z1
th = A*(1 - cos(w*t));             % angle turned by the plane Oxy [rad]
x1 = rho.*cos(th);
y1 = R*sin(phi);
z1 = -rho.*sin(th);

fprintf('\n=== Point 6: trajectory in Ox1y1z1 ===\n');
fprintf('theta in [%.4f, %.4f] rad (2A = %.4f rad)\n', min(th), max(th), 2*A);
fprintf('max|sqrt(x1^2 + z1^2) - R(1 + cos(phi))| = %.1e m\n', max(abs(sqrt(x1.^2 + z1.^2) - rho)));
fprintf('max distance to the axis = %.4f m, min = %.1e m\n', max(rho), min(rho));

ang = linspace(0, 2*pi, 200);
fig = figure('Position', [100 100 900 480], 'Color', 'w');
try
    theme(fig, 'light');
end
subplot(1, 2, 1)
plot3(x1, z1, y1, 'b', 'LineWidth', 0.5); hold on
plot3(R*(1 + cos(ang)), 0*ang, R*sin(ang), 'k--')    % wire at t = 0
plot3([0 0], [0 0], [-1.3 1.3]*R, 'k-.')             % axis Oy1
plot3(x1(1), z1(1), y1(1), 'ko', 'MarkerFaceColor', 'k')
xlabel('$x_1$ [m]'); ylabel('$z_1$ [m]'); zlabel('$y_1$ [m]'); title('(a)')
axis equal; grid on; view(35, 20)
subplot(1, 2, 2)
plot(x1, z1, 'b', 'LineWidth', 0.5); hold on
plot(0, 0, 'k+', 'MarkerSize', 10)
xlabel('$x_1$ [m]'); ylabel('$z_1$ [m]'); title('(b)')
axis equal; grid on
exportgraphics(fig, 'figures/point6.png', 'Resolution', 200)

% animation of the first period (bonus)
tv = 0:0.25:Tp;
phiv = interp1(t, phi, tv);
thv = A*(1 - cos(w*tv));
xv = R*(1 + cos(phiv)).*cos(thv);
yv = R*sin(phiv);
zv = -R*(1 + cos(phiv)).*sin(thv);
vid = VideoWriter('trajectory_P.mp4', 'MPEG-4');
vid.FrameRate = 30;
open(vid)
fig = figure('Position', [100 100 640 480], 'Color', 'w');
try
    theme(fig, 'light');
end
for k = 1:length(tv)
    clf
    plot3(xv(1:k), zv(1:k), yv(1:k), 'b', 'LineWidth', 0.5); hold on
    plot3(R*(1 + cos(ang))*cos(thv(k)), -R*(1 + cos(ang))*sin(thv(k)), R*sin(ang), 'k')
    plot3([0 0], [0 0], [-1.3 1.3]*R, 'k-.')
    plot3(xv(k), zv(k), yv(k), 'ro', 'MarkerFaceColor', 'r')
    axis equal; grid on; view(35, 20)
    axis([-2.1 2.1 -2.1 2.1 -1.3 1.3]*R)
    xlabel('$x_1$ [m]'); ylabel('$z_1$ [m]'); zlabel('$y_1$ [m]')
    title(sprintf('$t$ = %.1f s', tv(k)))
    % print gives frames of the same size every time
    writeVideo(vid, print(fig, '-RGBImage', '-r0'))
end
close(vid)
close(fig)
fprintf('video trajectory_P.mp4: %d frames, %.1f s of motion\n', length(tv), tv(end));

%% Point 7: fixed loop (A = 0)
phi0_list = [0 pi/4 pi/2];         % [rad]
phidot0_list = [0 1.5 3];          % [rad/s]
tf7 = 10;                          % [s]
cols = turbo(9);

fprintf('\n=== Point 7: A = 0, R = %.0f m, t in [0, %.0f] s ===\n', R, tf7);
fprintf('phi0 [rad]  phidot0 [rad/s]  phidot_c [rad/s]  prediction  simulation  max|E-E0|/(mgR)\n');
fig = figure('Position', [100 100 900 480], 'Color', 'w');
try
    theme(fig, 'light');
end
hold on
c = 0;
for i = 1:3
    for j = 1:3
        c = c + 1;
        p0 = phi0_list(i);
        pd0 = phidot0_list(j);
        [t7, X7] = ode45(@(t, X) diffeq(t, X, g, w, R, 0), [0 tf7], [p0; pd0], options);
        E7 = 0.5*m*R^2*X7(:, 2).^2 + m*g*R*sin(X7(:, 1));
        % analytical criterion (energy at the top phi = pi/2)
        pdc = sqrt(2*g/R*(1 - sin(p0)));
        if pd0 > pdc
            pred = 'rotates';
        elseif pd0 == pdc
            pred = 'rest';
        else
            pred = 'oscillates';
        end
        % what the simulation does
        if max(abs(X7(:, 2))) < 1e-6
            sim = 'rest';
        elseif all(X7(:, 2) > 0)
            sim = 'rotates';
        else
            sim = 'oscillates';
        end
        fprintf('%8.4f  %10.1f  %16.3f  %12s  %10s  %10.1e\n', p0, pd0, pdc, pred, sim, max(abs(E7 - E7(1)))/(m*g*R));
        % phi wrapped to [-3pi/2, pi/2) so that the rotations stay in the plot
        pw = mod(X7(:, 1) + 3*pi/2, 2*pi) - 3*pi/2;
        pw([false; abs(diff(pw)) > pi]) = NaN;
        plot(pw, X7(:, 2), 'Color', cols(c, :), 'DisplayName', sprintf('$(%.2f,\\ %.1f)$', p0, pd0))
        plot(p0, pd0, 'o', 'Color', cols(c, :), 'MarkerFaceColor', cols(c, :), 'HandleVisibility', 'off')
    end
end
ps = linspace(-3*pi/2, pi/2, 400);
plot(ps, sqrt(2*g/R*(1 - sin(ps))), 'k--', 'DisplayName', 'separatrix')
plot(ps, -sqrt(2*g/R*(1 - sin(ps))), 'k--', 'HandleVisibility', 'off')
xlabel('$\varphi$ [rad]'); ylabel('$\dot\varphi$ [rad/s]')
xlim([-3*pi/2 pi/2]); grid on
legend('Location', 'eastoutside')
exportgraphics(fig, 'figures/point7.png', 'Resolution', 200)

%% Point 8: linearized equation, phi = delta - pi/2
A = 0.1;
R = 0.01;                          % [m]
wn = sqrt(g/R);                    % natural frequency [rad/s]
w_list = [1 1/2 1/4]*wn;
t8 = linspace(0, 10, 5001)';       % common time grid [s]
names = {'$\omega=\omega_n$', '$\omega=\omega_n/2$', '$\omega=\omega_n/4$'};

fprintf('\n=== Point 8: A = %.1f, R = %.2f m, delta(0) = 0, deltadot(0) = 0 ===\n', A, R);
fprintf('omega_n = sqrt(g/R) = %.2f rad/s\n', wn);
fig = figure('Position', [100 100 900 480], 'Color', 'w');
try
    theme(fig, 'light');
end
for k = 1:3
    w = w_list(k);
    [~, Xf] = ode45(@(t, X) diffeq(t, X, g, w, R, A), t8, [-pi/2; 0], options);
    [~, Xl] = ode45(@(t, X) diffeqlin(t, X, g, w, R, A), t8, [0; 0], options);
    df = Xf(:, 1) + pi/2;          % delta of the full equation
    dl = Xl(:, 1);
    err = 100*abs(dl - df)/max(abs(df));
    fprintf('omega = %.4f rad/s: A^2 = %.3f vs g/(R omega^2) = %.0f, max|delta_full| = %.4f rad, max|delta_lin| = %.4f rad\n', ...
        w, A^2, g/(R*w^2), max(abs(df)), max(abs(dl)));
    fprintf('   error at t = 5 s = %.2f %%, max error = %.2f %%\n', err(t8 == 5), max(err));
    % dropped term Omega^2*delta: mean of Omega^2 is A^2 omega^2/2, it lowers the stiffness g/R
    fprintf('   mean(Omega^2) = A^2 omega^2/2 = %.3f s^-2 = %.3f %% of g/R, frequency shift = %.3f %%, phase lag in 10 s = %.2f rad\n', ...
        A^2*w^2/2, 100*A^2*w^2/2/(g/R), 100*A^2*w^2/4/(g/R), A^2*w^2/4/(g/R)*wn*10);
    subplot(1, 2, 1)
    plot(t8, err, 'LineWidth', 1); hold on
    if k == 2
        subplot(1, 2, 2)
        plot(t8, df, 'b'); hold on
        plot(t8, dl, 'r--')
        plot(t8, A^2*w^2/(4*wn)*t8, 'k:', t8, -A^2*w^2/(4*wn)*t8, 'k:')
        fprintf('   resonance envelope A^2 omega^2 t/(4 omega_n) at t = 10 s = %.4f rad\n', A^2*w^2/(4*wn)*10);
    end
end
subplot(1, 2, 1)
xlabel('$t$ [s]'); ylabel('error [\%]'); title('(a)')
legend(names, 'Location', 'northwest'); grid on
subplot(1, 2, 2)
xlabel('$t$ [s]'); ylabel('$\delta$ [rad]'); title('(b) $\omega=\omega_n/2$')
legend('full', 'linear', 'envelope', 'Location', 'southwest'); grid on
xlim([7 10])
exportgraphics(fig, 'figures/point8.png', 'Resolution', 200)

%% Functions
function Xdot = diffeq(t, X, g, omega, R, A)
phi = X(1);
phidot = X(2);
Om = A*omega*sin(omega*t);
phiddot = -g/R*cos(phi) - Om^2*(1 + cos(phi))*sin(phi);
Xdot = [phidot; phiddot];
end

function Xdot = diffeqlin(t, X, g, omega, R, A)
% X = [delta; deltadot], linearized equation around the bottom
delta = X(1);
Om = A*omega*sin(omega*t);
deltaddot = -g/R*delta + Om^2;
Xdot = [X(2); deltaddot];
end
