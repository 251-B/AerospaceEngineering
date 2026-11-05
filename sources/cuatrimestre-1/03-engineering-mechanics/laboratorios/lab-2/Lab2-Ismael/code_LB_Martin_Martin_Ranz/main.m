%% Laboratory 2: Particle on oscillating loop
% Mechanics Applied to Aerospace Engineering, UC3M
% Group LB: Ismael Martin Diez, David Martin Garcia, Alejandro Ranz Remartinez
clc
clear
close all

% Plot formatting (Script 6 of the guidelines). The figures are drawn at the
% size they have in the report, so these fonts are the printed ones
set(groot, 'defaultLegendFontSize', 10);
set(groot, 'defaultTextFontSize', 10);
set(groot, 'defaultAxesFontSize', 10);
set(groot, 'defaultAxesLineWidth', 0.75);
set(groot, 'defaultAxesXMinorTick', 'on');
set(groot, 'defaultAxesYMinorTick', 'on');
set(groot, 'defaultLegendBox', 'off');
set(groot, 'defaultLineLineWidth', 1);
set(groot, 'defaultLineMarkerSize', 5);
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');

if ~isfolder('figures')
    mkdir('figures')
end

options = odeset('RelTol', 1e-8, 'AbsTol', 1e-10, 'MaxStep', 0.01);
g = 9.81;          % gravity [m/s^2]
m = 1;             % mass [kg]

%% Point 5: oscillating loop
A = pi;            % [-]
w = 0.1;           % omega [rad/s]
R = 1;             % radius of the wire [m]
T = 2*pi/w;        % period of the rotating frame [s]
X0 = [0; 0];       % [phi(0); phidot(0)]

[t, X] = ode45(@(t, X) diffeq(t, X, g, w, R, A), [0 3*T], X0, options);
phi = X(:, 1);
phidot = X(:, 2);

% formulas of the report
Om = A*w*sin(w*t);                  % Omega(t) [rad/s]
Omdot = A*w^2*cos(w*t);             % dOmega/dt [rad/s^2]
x = R*(1 + cos(phi));               % distance from P to the axis Oy [m]
Fcent = m*Om.^2.*x;                 % along i
Feul = m*Omdot.*x;                  % along k
Fcor = -2*m*Om*R.*phidot.*sin(phi); % along k
N1 = -m*R*phidot.^2 + m*g*sin(phi) - m*Om.^2.*x.*cos(phi);
N2 = 2*m*Om*R.*phidot.*sin(phi) - m*Omdot.*x;
Ek = 0.5*m*(R^2*phidot.^2 + Om.^2.*x.^2);
Ep = m*g*R*sin(phi);
E = Ek + Ep;
Wire = cumtrapz(t, -Om.*x.*N2);     % work of the wire, integral of N.v [J]

% swing period, from the lowest values of phi
tmin = t(islocalmin(phi));
Tsw = mean(diff(tmin));
K = ellipke(0.5);                   % complete elliptic integral, amplitude 90 deg
[~, iE] = max(E - E(1));

fprintf('\n=== Point 5: A = pi, omega = %.1f rad/s, R = %.0f m ===\n', w, R);
fprintf('T = 2*pi/omega = %.2f s, 3T = %.1f s, at least %.0f steps per swing\n', T, 3*T, Tsw/0.01);
fprintf('max|Omega| = A*omega = %.4f rad/s, max|dOmega/dt| = A*omega^2 = %.4f rad/s^2\n', A*w, A*w^2);
fprintf('(A*omega)^2/(g/R) = %.2f %%, A^2 = %.2f vs g/(R*omega^2) = %.0f\n', 100*(A*w)^2/(g/R), A^2, g/(R*w^2));
Xd0 = diffeq(0, X0, g, w, R, A);
fprintf('phiddot(0) = %.2f rad/s^2 (-g/R = %.2f)\n', Xd0(2), -g/R);
fprintf('phi in [%.4f, %.4f] rad, phidot in [%.3f, %.3f] rad/s\n', min(phi), max(phi), min(phidot), max(phidot));
fprintf('highest point: R*sin(max(phi)) = %.4f m\n', R*sin(max(phi)));
fprintf('swing period = %.3f s, small oscillations 2*pi*sqrt(R/g) = %.3f s, exact 90 deg pendulum 4*sqrt(R/g)*K = %.3f s\n', Tsw, 2*pi*sqrt(R/g), 4*sqrt(R/g)*K);
fprintf('swings in 3T = %.1f, swings in T = %.1f\n', 3*T/Tsw, T/Tsw);
fprintf('N1 in [%.2f, %.2f] N, -3mg = %.2f N\n', min(N1), max(N1), -3*m*g);
fprintf('N2 in [%.3f, %.3f] N, max|N1|/max|N2| = %.1f\n', min(N2), max(N2), max(abs(N1))/max(abs(N2)));
fprintf('max|F_cent| = %.4f N, 2mA^2omega^2R = %.4f N, F_cent/(mg) = %.2f %%\n', max(abs(Fcent)), 2*m*(A*w)^2*R, 100*max(abs(Fcent))/(m*g));
fprintf('max|F_Euler| = %.4f N, 2mA*omega^2*R = %.4f N\n', max(abs(Feul)), 2*m*A*w^2*R);
fprintf('max|F_Cor| = %.3f N, 2mA*omega*R*max|phidot| = %.3f N, max|F_Cor|/max|F_Euler| = %.1f\n', max(abs(Fcor)), 2*m*A*w*R*max(abs(phidot)), max(abs(Fcor))/max(abs(Feul)));
fprintf('Ek in [%.3f, %.3f] J, Ep in [%.3f, %.3f] J\n', min(Ek), max(Ek), min(Ep), max(Ep));
fprintf('E(0) = %.4f J, E - E0 in [%.4f, %.4f] J, largest at t = %.1f s\n', E(1), min(E - E(1)), max(E - E(1)), t(iE));
fprintf('E - E0 at T, 2T, 3T = %.4f, %.4f, %.4f J\n', interp1(t, E, T) - E(1), interp1(t, E, 2*T) - E(1), E(end) - E(1));
fprintf('max|E - E0 - W_wire| = %.1e J\n', max(abs(E - E(1) - Wire)));
fprintf('max|x*N2| = %.3f N m\n', max(abs(x.*N2)));
fprintf('range of E = %.4f J, jump from x = 0 to x = 2R at max Omega, 4m(A*omega)^2*R^2 = %.4f J\n', max(E) - min(E), 4*m*(A*w)^2*R^2);

% E = J + m*Omega^2*x^2 with dJ/dt = -dOmega/dt*L, so J follows -m*Omega^2*mean(x^2)/2
x2mean = trapz(t, x.^2)/t(end);     % time average of x^2 [m^2]
fprintf('mean(x^2) = %.3f m^2, estimate of E - E0 at the maximum Omega: x = 0: %.4f J, x = 2R: %.4f J\n', x2mean, -0.5*m*(A*w)^2*x2mean, m*(A*w)^2*(4*R^2 - 0.5*x2mean));

zoom5 = [T/4 - 5, T/4 + 5];         % window around t = T/4, where the plane turns fastest
fprintf('zoom window = [%.1f, %.1f] s\n', zoom5(1), zoom5(2));

% Figure: angle and reaction forces
fig = figure('Units', 'centimeters', 'Position', [2 2 17 8.0], 'Color', 'w');
try
    theme(fig, 'light');
end
subplot(3, 2, 1)
plot(t, phi, 'b', 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(a)')
xlim([0 3*T]); ylim([-3.5 0.5]); grid on
subplot(3, 2, 2)
plot(t, phi, 'b')
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(b)')
xlim(zoom5); ylim([-3.5 0.5]); grid on
subplot(3, 2, 3)
plot(t, N1, 'b', 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('$N_1$ (N)'); title('(c)')
xlim([0 3*T]); ylim([-32 2]); grid on
subplot(3, 2, 4)
plot(t, N1, 'b')
xlabel('$t$ (s)'); ylabel('$N_1$ (N)'); title('(d)')
xlim(zoom5); ylim([-32 2]); grid on
subplot(3, 2, 5)
plot(t, N2, 'r', 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('$N_2$ (N)'); title('(e)')
xlim([0 3*T]); ylim([-3 3]); grid on
subplot(3, 2, 6)
plot(t, N2, 'r')
xlabel('$t$ (s)'); ylabel('$N_2$ (N)'); title('(f)')
xlim(zoom5); ylim([-3 3]); grid on
exportgraphics(fig, 'figures/angle_reactions.png', 'Resolution', 300)

% Figure: inertia forces, each with its own axis because their sizes differ
fig = figure('Units', 'centimeters', 'Position', [2 2 17 6.2], 'Color', 'w');
try
    theme(fig, 'light');
end
subplot(2, 2, 1)
plot(t, Fcent, 'k', 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('$F_{cent}$ (N)'); title('(a)')
xlim([0 3*T]); ylim([0 0.25]); grid on
subplot(2, 2, 2)
plot(t, Feul, 'Color', [0 0.5 0], 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('$F_{Euler}$ (N)'); title('(b)')
xlim([0 3*T]); ylim([-0.08 0.08]); grid on
subplot(2, 2, 3)
plot(t, Fcor, 'r', 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('$F_{Cor}$ (N)'); title('(c)')
xlim([0 3*T]); ylim([-3 3]); grid on
subplot(2, 2, 4)
plot(t, Fcor, 'r'); hold on
plot(t, N2, 'k--')
xlabel('$t$ (s)'); ylabel('$F_{Cor}$, $N_2$ (N)'); title('(d)')
legend('$F_{Cor}$', '$N_2$', 'Location', 'north', 'Orientation', 'horizontal')
xlim(zoom5); ylim([-3 5]); grid on
exportgraphics(fig, 'figures/inertia_forces.png', 'Resolution', 300)

% Figure: energies
fig = figure('Units', 'centimeters', 'Position', [2 2 17 6.2], 'Color', 'w');
try
    theme(fig, 'light');
end
subplot(2, 2, 1)
plot(t, Ek, 'b', 'LineWidth', 0.5); hold on
plot(t, Ep, 'r', 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('Energy (J)'); title('(a)')
legend('$E_k$', '$E_p$', 'Location', 'north', 'Orientation', 'horizontal')
xlim([0 3*T]); ylim([-12 20]); grid on
subplot(2, 2, 2)
plot(t, Ek, 'b'); hold on
plot(t, Ep, 'r')
xlabel('$t$ (s)'); ylabel('Energy (J)'); title('(b)')
legend('$E_k$', '$E_p$', 'Location', 'north', 'Orientation', 'horizontal')
xlim(zoom5); ylim([-12 20]); grid on
subplot(2, 2, 3)
plot(t, E - E(1), 'k', 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('$E-E_0$ (J)'); title('(c)')
xlim([0 3*T]); ylim([-0.1 0.35]); grid on
subplot(2, 2, 4)
plot(t, E - E(1), 'k')
xlabel('$t$ (s)'); ylabel('$E-E_0$ (J)'); title('(d)')
xlim(zoom5); ylim([-0.1 0.35]); grid on
exportgraphics(fig, 'figures/energies.png', 'Resolution', 300)

%% Point 6: trajectory in the fixed frame Ox1y1z1
th = A*(1 - cos(w*t));              % angle turned by the plane Oxy [rad]
x1 = x.*cos(th);
y1 = R*sin(phi);
z1 = -x.*sin(th);

fprintf('\n=== Point 6: trajectory in Ox1y1z1 ===\n');
fprintf('theta in [%.4f, %.4f] rad (2A = %.4f rad)\n', min(th), max(th), 2*A);
fprintf('largest turn of the plane in one swing = A*omega*Tsw = %.3f rad\n', A*w*Tsw);
fprintf('max|sqrt(x1^2 + z1^2) - R(1 + cos(phi))| = %.1e m\n', max(abs(sqrt(x1.^2 + z1.^2) - x)));
fprintf('distance to the axis in [%.1e, %.4f] m\n', min(x), max(x));

ang = linspace(0, 2*pi, 200);       % points of the wire
fig = figure('Units', 'centimeters', 'Position', [2 2 17 6.2], 'Color', 'w');
try
    theme(fig, 'light');
end
subplot(1, 2, 1)
plot3(x1, z1, y1, 'b', 'LineWidth', 0.35); hold on
plot3(R*(1 + cos(ang)), 0*ang, R*sin(ang), 'k--')    % wire at t = 0
plot3([0 0], [0 0], [-1.3 1.3]*R, 'k-.')             % axis Oy1
plot3(x1(1), z1(1), y1(1), 'ko', 'MarkerFaceColor', 'k')
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); zlabel('$y_1$ (m)'); title('(a)')
axis equal; grid on; view(35, 20)
set(gca, 'YDir', 'reverse')         % keeps the frame right-handed with y1 upward
subplot(1, 2, 2)
plot(x1, z1, 'b', 'LineWidth', 0.35); hold on
plot(x1(1), z1(1), 'ko', 'MarkerFaceColor', 'k')
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); title('(b)')
axis equal; grid on
set(gca, 'YDir', 'reverse')         % seen from above, z1 points down the page
exportgraphics(fig, 'figures/trajectory.png', 'Resolution', 300)

% Animation of the first period (bonus of the slides)
tv = 0:0.2:T;
vid = VideoWriter('trajectory_video.avi', 'Motion JPEG AVI');   % available on every system
vid.FrameRate = 15;
vid.Quality = 50;
open(vid)
fig = figure('Position', [100 100 560 420], 'Color', 'w');
try
    theme(fig, 'light');
end
plot3([0 0], [0 0], [-1.3 1.3]*R, 'k-.'); hold on
hWire = plot3(R*(1 + cos(ang)), 0*ang, R*sin(ang), 'k', 'LineWidth', 1.5);
hPath = plot3(x1(1), z1(1), y1(1), 'b', 'LineWidth', 0.5);
hP = plot3(x1(1), z1(1), y1(1), 'ro', 'MarkerFaceColor', 'r', 'MarkerSize', 7);
axis equal; grid on; view(35, 20)
axis([-2.1 2.1 -2.1 2.1 -1.3 1.3]*R)
set(gca, 'YDir', 'reverse')
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); zlabel('$y_1$ (m)')
for k = 1:length(tv)
    n = find(t <= tv(k), 1, 'last');
    set(hWire, 'XData', R*(1 + cos(ang))*cos(th(n)), 'YData', -R*(1 + cos(ang))*sin(th(n)))
    set(hPath, 'XData', x1(1:n), 'YData', z1(1:n), 'ZData', y1(1:n))
    set(hP, 'XData', x1(n), 'YData', z1(n), 'ZData', y1(n))
    title(sprintf('$t$ = %.1f s, $\\theta$ = %.2f rad', t(n), th(n)))
    % print gives frames of the same size every time (getframe may not)
    writeVideo(vid, print(fig, '-RGBImage', '-r0'))
end
close(vid)
close(fig)
fprintf('video trajectory_video.avi: %d frames, first period T = %.1f s of motion\n', length(tv), tv(end));

%% Point 7: fixed loop (A = 0)
phi0_list = [0 pi/4 pi/2];          % [rad]
phidot0_list = [0 1.5 3];           % [rad/s]
phi_names = ["0", "\pi/4", "\pi/2"];
colors = {'b', 'r', [0 0.5 0]};     % one colour for each phi(0)
styles = {'-', '--', ':'};          % one line style for each phidot(0)
tf7 = 10;                           % [s]

fprintf('\n=== Point 7: A = 0, R = %.0f m, t in [0, %.0f] s ===\n', R, tf7);
fprintf('cos(pi/2) in the computer = %.1e\n', cos(pi/2));
fprintf('phi0[rad] phidot0[rad/s] E0/(mgR) phidot_c[rad/s] prediction simulation phimax_pred phimax_sim period[s] max|phidot|[rad/s] max|E-E0|/(mgR)\n');
fig = figure('Units', 'centimeters', 'Position', [2 2 17 6.6], 'Color', 'w');
try
    theme(fig, 'light');
end
hold on
for i = 1:3
    for j = 1:3
        p0 = phi0_list(i);
        pd0 = phidot0_list(j);
        [t7, X7] = ode45(@(t, X) diffeq(t, X, g, w, R, 0), 0:0.001:tf7, [p0; pd0], options);
        E7 = 0.5*m*R^2*X7(:, 2).^2 + m*g*R*sin(X7(:, 1));
        % analytical criterion: energy against the top of the loop, phi = pi/2
        pdc = sqrt(2*g/R*(1 - sin(p0)));
        E0 = 0.5*m*R^2*pd0^2 + m*g*R*sin(p0);
        if pd0 > pdc
            pred = 'rotates';
            pmax_pred = NaN;
        elseif pd0 == pdc
            pred = 'rest';
            pmax_pred = p0;
        else
            pred = 'oscillates';
            pmax_pred = asin(sin(p0) + R*pd0^2/(2*g));
        end
        % what the simulation does
        Tosc = NaN;
        if max(abs(X7(:, 2))) < 1e-6
            obs = 'rest';
        elseif all(X7(:, 2) > 0)
            obs = 'rotates';
        else
            obs = 'oscillates';
            Tosc = mean(diff(t7(islocalmax(X7(:, 1)))));
        end
        fprintf('%7.4f %8.1f %12.3f %12.3f %12s %10s %9.4f %10.4f %9.3f %11.1e %11.1e\n', p0, pd0, E0/(m*g*R), pdc, ...
            pred, obs, pmax_pred, max(X7(:, 1)), Tosc, max(abs(X7(:, 2))), max(abs(E7 - E7(1)))/(m*g*R));
        % phi wrapped to [-3pi/2, pi/2), both ends are the top of the loop
        pw = mod(X7(:, 1) + 3*pi/2, 2*pi) - 3*pi/2;
        pw([false; abs(diff(pw)) > pi]) = NaN;
        plot(pw, X7(:, 2), styles{j}, 'Color', colors{i}, 'DisplayName', sprintf('$\\varphi_0=%s$, $\\dot\\varphi_0=%.1f$', phi_names(i), pd0))
        plot(p0, pd0, 'o', 'Color', colors{i}, 'MarkerFaceColor', colors{i}, 'HandleVisibility', 'off')
    end
end
% the rest at the top only lasts while each step of phi is below its rounding
[t7, X7] = ode45(@(t, X) diffeq(t, X, g, w, R, 0), [0 40], [pi/2; 0], options);
fprintf('top of the loop with phidot(0) = 0: phi first changes at t = %.2f s and reaches phi = 0 at t = %.1f s\n', t7(find(X7(:, 1) ~= pi/2, 1)), t7(find(X7(:, 1) < 0, 1)));
ps = linspace(-3*pi/2, pi/2, 400);
plot(ps, sqrt(2*g/R*(1 - sin(ps))), 'k-.', 'DisplayName', 'separatrix')
plot(ps, -sqrt(2*g/R*(1 - sin(ps))), 'k-.', 'HandleVisibility', 'off')
plot(-pi/2, 0, 'k+', 'MarkerSize', 8, 'DisplayName', 'stable equilibrium')
xlabel('$\varphi$ (rad)'); ylabel('$\dot\varphi$ (rad/s)')
xlim([-3*pi/2 pi/2]); ylim([-8 8]); grid on
xticks(-3*pi/2:pi/2:pi/2); xticklabels({'$-3\pi/2$', '$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$'})
legend('Location', 'eastoutside', 'FontSize', 9)
exportgraphics(fig, 'figures/phase_portrait.png', 'Resolution', 300)

%% Point 8: linearized equation, phi = delta - pi/2
A = 0.1;
R = 0.01;                           % [m]
wn = sqrt(g/R);                     % natural frequency [rad/s]
w_list = [1 1/2 1/4]*wn;
t8 = linspace(0, 10, 5001)';        % common time grid [s], 100 points per natural period
col8 = [0 0 1; 1 0 0; 0 0.5 0];
light8 = 0.3*col8 + 0.7;            % lighter tone for the raw error
names = ["$\omega=\omega_n$", "$\omega=\omega_n/2$", "$\omega=\omega_n/4$"];

fprintf('\n=== Point 8: A = %.1f, R = %.2f m, delta(0) = 0, deltadot(0) = 0 ===\n', A, R);
fprintf('omega_n = sqrt(g/R) = %.2f rad/s, g/R = %.0f s^-2, natural period = %.3f s, natural periods in 10 s = %.1f\n', wn, g/R, 2*pi/wn, 10*wn/(2*pi));
fig = figure('Units', 'centimeters', 'Position', [2 2 17 7.8], 'Color', 'w');
try
    theme(fig, 'light');
end
amp8 = zeros(1, 3);                 % largest delta of each case [rad]
for k = 1:3
    w = w_list(k);
    [~, Xf] = ode45(@(t, X) diffeq(t, X, g, w, R, A), t8, [-pi/2; 0], options);
    [~, Xl] = ode45(@(t, X) diffeqlin(t, X, g, w, R, A), t8, [0; 0], options);
    df = Xf(:, 1) + pi/2;           % delta of the full equation
    dl = Xl(:, 1);                  % delta of the linearized equation
    err = 100*abs(dl - df)/max(abs(df));
    amp8(k) = max(abs(df));

    % closed form of the linearized equation
    F0 = A^2*w^2/2;
    if k == 2
        dex = F0/wn^2*(1 - cos(wn*t8)) - F0/(2*wn)*t8.*sin(wn*t8);
    else
        dex = F0/wn^2 - F0*cos(2*w*t8)/(wn^2 - 4*w^2) + (F0/(wn^2 - 4*w^2) - F0/wn^2)*cos(wn*t8);
    end

    % which approximation causes the error: put back each neglected term alone
    [~, Xa] = ode45(@(t, X) [X(2); -g/R*X(1) + (A*w*sin(w*t))^2*(1 + X(1))], t8, [0; 0], options);
    [~, Xb] = ode45(@(t, X) [X(2); -g/R*sin(X(1)) + (A*w*sin(w*t))^2], t8, [0; 0], options);

    fprintf('omega = %.2f rad/s: A^2 = %.2f vs g/(R omega^2) = %.0f, forcing frequency 2*omega = %.2f rad/s\n', w, A^2, g/(R*w^2), 2*w);
    fprintf('   delta_s = F0/omega_n^2 = %.5f rad\n', F0/wn^2);
    fprintf('   max|delta_full| = %.5f rad, max|delta_lin| = %.5f rad, max|delta_lin - closed form| = %.1e rad\n', max(abs(df)), max(abs(dl)), max(abs(dl - dex)));
    fprintf('   largest error in [0, 5] s = %.2f %%, in [0, 10] s = %.2f %%\n', max(err(t8 <= 5)), max(err));
    fprintf('   largest error keeping Omega^2*delta = %.3f %%, keeping sin(delta) = %.3f %%\n', ...
        100*max(abs(Xa(:, 1) - df))/max(abs(df)), 100*max(abs(Xb(:, 1) - df))/max(abs(df)));
    fprintf('   mean(Omega^2) = A^2 omega^2/2 = %.3f s^-2 = %.3f %% of g/R\n', A^2*w^2/2, 100*A^2*w^2/2/(g/R));

    % another initial condition, away from the bottom
    [~, Xf1] = ode45(@(t, X) diffeq(t, X, g, w, R, A), t8, [0.1 - pi/2; 0], options);
    [~, Xl1] = ode45(@(t, X) diffeqlin(t, X, g, w, R, A), t8, [0.1; 0], options);
    fprintf('   with delta(0) = 0.1 rad: largest error = %.0f %%\n', 100*max(abs(Xl1(:, 1) - Xf1(:, 1) - pi/2))/max(abs(Xf1(:, 1) + pi/2)));

    subplot(2, 3, [1 2 3])
    semilogy(t8, err, 'Color', light8(k, :), 'LineWidth', 0.5, 'HandleVisibility', 'off'); hold on
    % thick line: upper envelope of the fast oscillation of the error
    semilogy(t8, movmax(err, 201), 'Color', col8(k, :), 'LineWidth', 1.5, 'DisplayName', names(k))
    if k == 1
        % natural part of delta in the last second: fit of c0 + c1*cos(2wt) + a*cos(wn*t) + b*sin(wn*t)
        i9 = t8 >= 9;
        Mfit = [ones(sum(i9), 1) cos(2*w*t8(i9)) cos(wn*t8(i9)) sin(wn*t8(i9))];
        cf = Mfit\df(i9);
        cl = Mfit\dl(i9);
        fprintf('   natural part in [9, 10] s: full lags %.2f rad, amplitude full/linear = %.3f, their difference = %.1f %% of max|delta_full|\n', ...
            mod(atan2(cf(4), cf(3)) - atan2(cl(4), cl(3)), 2*pi), hypot(cf(3), cf(4))/hypot(cl(3), cl(4)), 100*hypot(cf(3) - cl(3), cf(4) - cl(4))/max(abs(df)));
        subplot(2, 3, 6)
        plot(t8, 1e3*df, 'b'); hold on
        plot(t8, 1e3*dl, 'r--')
        xlabel('$t$ (s)'); ylabel('$\delta$ ($10^{-3}$ rad)'); title('(d) $\omega=\omega_n$')
        xlim([9 10]); grid on
    elseif k == 2
        subplot(2, 3, 4)
        plot(t8, df, 'b', 'LineWidth', 0.5); hold on
        plot(t8, F0/(2*wn)*t8, 'k--')
        plot(t8, -F0/(2*wn)*t8, 'k--', 'HandleVisibility', 'off')
        xlabel('$t$ (s)'); ylabel('$\delta$ (rad)'); title('(b) $\omega=\omega_n/2$')
        xlim([0 10]); ylim([-0.25 0.25]); grid on
        subplot(2, 3, 5)
        plot(t8, df, 'b'); hold on
        plot(t8, dl, 'r--')
        xlabel('$t$ (s)'); ylabel('$\delta$ (rad)'); title('(c) $\omega=\omega_n/2$')
        xlim([9 10]); ylim([-0.25 0.25]); grid on
        fprintf('   resonance envelope F0*t/(2*omega_n) at t = 10 s = %.4f rad\n', F0/(2*wn)*10);
    end
end
subplot(2, 3, [1 2 3])
xlabel('$t$ (s)'); ylabel('Error (\%)'); title('(a)')
ylim([1e-3 100]); yticks([1e-3 1e-2 1e-1 1 10 100]); grid on
set(gca, 'YMinorGrid', 'off')
legend('Location', 'southeast', 'Orientation', 'horizontal')
exportgraphics(fig, 'figures/linearized_error.png', 'Resolution', 300)
fprintf('max|delta| at resonance = %.1f deg = %.1f times the one at omega_n\n', amp8(2)*180/pi, amp8(2)/amp8(1));

% resonance for a longer time: the softening of the full equation detunes it from the forcing
w = wn/2;
[t100, X100] = ode45(@(t, X) diffeq(t, X, g, w, R, A), [0 100], [-pi/2; 0], options);
[d100, i100] = max(abs(X100(:, 1) + pi/2));
fprintf('full equation at resonance, t in [0, 100] s: max|delta| = %.3f rad at t = %.1f s, linearized envelope at 100 s = %.2f rad\n', d100, t100(i100), A^2*w^2/(4*wn)*100);

%% Functions
function Xdot = diffeq(t, X, g, omega, R, A)
% X = [phi; phidot], equation of motion of the report
phi = X(1);
phidot = X(2);
Om = A*omega*sin(omega*t);
phiddot = -g/R*cos(phi) - Om^2*(1 + cos(phi))*sin(phi);
Xdot = [phidot; phiddot];
end

function Xdot = diffeqlin(t, X, g, omega, R, A)
% X = [delta; deltadot], linearized equation around the bottom of the loop
delta = X(1);
deltadot = X(2);
Om = A*omega*sin(omega*t);
deltaddot = -g/R*delta + Om^2;
Xdot = [deltadot; deltaddot];
end
