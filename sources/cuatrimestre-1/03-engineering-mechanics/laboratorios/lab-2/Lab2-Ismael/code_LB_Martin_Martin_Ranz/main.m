%% Laboratory 2: Particle on oscillating loop
% Mechanics Applied to Aerospace Engineering, UC3M
% Group LB: Ismael Martin Diez, David Martin Garcia, Alejandro Ranz Remartinez
clc
clear
close all

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
g = 9.81;
m = 1;

%% Point 5: oscillating loop
A = pi;
w = 0.1;
R = 1;
T = 2*pi/w;
X0 = [0; 0];

[t, X] = ode45(@(t, X) diffeq(t, X, g, w, R, A), [0 3*T], X0, options);
phi = X(:, 1);
phidot = X(:, 2);

Om = A*w*sin(w*t);
Omdot = A*w^2*cos(w*t);
x = R*(1 + cos(phi));
Fcent = m*Om.^2.*x;
Feul = m*Omdot.*x;
Fcor = -2*m*Om*R.*phidot.*sin(phi);
N1 = -m*R*phidot.^2 + m*g*sin(phi) - m*Om.^2.*x.*cos(phi);
N2 = 2*m*Om*R.*phidot.*sin(phi) - m*Omdot.*x;
K = 0.5*m*(R^2*phidot.^2 + Om.^2.*x.^2);
V = m*g*R*sin(phi);
E = K + V;

Tsw = mean(diff(t(islocalmin(phi))));

fprintf('\n=== Point 5 ===\n');
fprintf('T = %.2f s\n', T);
fprintf('phi in [%.2f, %.2f] rad, max|phidot| = %.2f rad/s\n', min(phi), max(phi), max(abs(phidot)));
fprintf('swing period = %.2f s, small oscillations = %.2f s\n', Tsw, 2*pi*sqrt(R/g));
fprintf('N1 in [%.2f, %.2f] N, -3mg = %.2f N\n', min(N1), max(N1), -3*m*g);
fprintf('max|N2| = %.2f N\n', max(abs(N2)));
fprintf('max F_cent = %.2f N, max|F_Euler| = %.2f N, max|F_Cor| = %.2f N\n', max(abs(Fcent)), max(abs(Feul)), max(abs(Fcor)));
fprintf('max K = %.2f J, V in [%.2f, %.2f] J\n', max(K), min(V), max(V));
fprintf('E - E(0) in [%.2f, %.2f] J\n', min(E - E(1)), max(E - E(1)));
fprintf('E - E(0) at T, 2T, 3T = %.3f, %.3f, %.3f J\n', interp1(t, E, T) - E(1), interp1(t, E, 2*T) - E(1), E(end) - E(1));

zoom5 = [T/4 - 5, T/4 + 5];

fig = figure('Units', 'centimeters', 'Position', [2 2 17 9.5], 'Color', 'w');
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

fig = figure('Units', 'centimeters', 'Position', [2 2 17 7], 'Color', 'w');
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

fig = figure('Units', 'centimeters', 'Position', [2 2 17 7], 'Color', 'w');
try
    theme(fig, 'light');
end
subplot(2, 2, 1)
plot(t, K, 'b', 'LineWidth', 0.5); hold on
plot(t, V, 'r', 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('Energy (J)'); title('(a)')
legend('$K_0^P$', '$V_0^P$', 'Location', 'north', 'Orientation', 'horizontal')
xlim([0 3*T]); ylim([-12 20]); grid on
subplot(2, 2, 2)
plot(t, K, 'b'); hold on
plot(t, V, 'r')
xlabel('$t$ (s)'); ylabel('Energy (J)'); title('(b)')
legend('$K_0^P$', '$V_0^P$', 'Location', 'north', 'Orientation', 'horizontal')
xlim(zoom5); ylim([-12 20]); grid on
subplot(2, 2, 3)
plot(t, E - E(1), 'k', 'LineWidth', 0.5)
xlabel('$t$ (s)'); ylabel('$E_0^P-E_{0,1}^P$ (J)'); title('(c)')
xlim([0 3*T]); ylim([-0.1 0.35]); grid on
subplot(2, 2, 4)
plot(t, E - E(1), 'k')
xlabel('$t$ (s)'); ylabel('$E_0^P-E_{0,1}^P$ (J)'); title('(d)')
xlim(zoom5); ylim([-0.1 0.35]); grid on
exportgraphics(fig, 'figures/energies.png', 'Resolution', 300)

%% Point 6: trajectory in the fixed frame
th = A*(1 - cos(w*t));
x0 = x.*cos(th);
y0 = R*sin(phi);
z0 = -x.*sin(th);

ang = linspace(0, 2*pi, 200);
fig = figure('Units', 'centimeters', 'Position', [2 2 17 7], 'Color', 'w');
try
    theme(fig, 'light');
end
subplot(1, 2, 1)
plot3(x0, z0, y0, 'b', 'LineWidth', 0.35); hold on
plot3(R*(1 + cos(ang)), 0*ang, R*sin(ang), 'k--')
plot3([0 0], [0 0], [-1.3 1.3]*R, 'k-.')
plot3(x0(1), z0(1), y0(1), 'ko', 'MarkerFaceColor', 'k')
xlabel('$x_0$ (m)'); ylabel('$z_0$ (m)'); zlabel('$y_0$ (m)'); title('(a)')
axis equal; grid on; view(35, 20)
set(gca, 'YDir', 'reverse')     % right-handed axes
subplot(1, 2, 2)
plot(x0, z0, 'b', 'LineWidth', 0.35); hold on
plot(x0(1), z0(1), 'ko', 'MarkerFaceColor', 'k')
xlabel('$x_0$ (m)'); ylabel('$z_0$ (m)'); title('(b)')
axis equal; grid on
set(gca, 'YDir', 'reverse')
exportgraphics(fig, 'figures/trajectory.png', 'Resolution', 300)

% video of the first period
tv = 0:0.2:T;
vid = VideoWriter('trajectory_video.avi', 'Motion JPEG AVI');
vid.FrameRate = 15;
vid.Quality = 50;
open(vid)
fig = figure('Position', [100 100 560 420], 'Color', 'w');
try
    theme(fig, 'light');
end
plot3([0 0], [0 0], [-1.3 1.3]*R, 'k-.'); hold on
hWire = plot3(R*(1 + cos(ang)), 0*ang, R*sin(ang), 'k', 'LineWidth', 1.5);
hPath = plot3(x0(1), z0(1), y0(1), 'b', 'LineWidth', 0.5);
hP = plot3(x0(1), z0(1), y0(1), 'ro', 'MarkerFaceColor', 'r', 'MarkerSize', 7);
axis equal; grid on; view(35, 20)
axis([-2.1 2.1 -2.1 2.1 -1.3 1.3]*R)
set(gca, 'YDir', 'reverse')
xlabel('$x_0$ (m)'); ylabel('$z_0$ (m)'); zlabel('$y_0$ (m)')
for k = 1:length(tv)
    n = find(t <= tv(k), 1, 'last');
    set(hWire, 'XData', R*(1 + cos(ang))*cos(th(n)), 'YData', -R*(1 + cos(ang))*sin(th(n)))
    set(hPath, 'XData', x0(1:n), 'YData', z0(1:n), 'ZData', y0(1:n))
    set(hP, 'XData', x0(n), 'YData', z0(n), 'ZData', y0(n))
    title(sprintf('$t$ = %.1f s, $\\theta$ = %.2f rad', t(n), th(n)))
    writeVideo(vid, print(fig, '-RGBImage', '-r0'))     % same frame size
end
close(vid)
close(fig)

%% Point 7: fixed loop (A = 0)
phi0_list = [0 pi/4 pi/2];
phidot0_list = [0 1.5 3];
phi_names = ["0", "\pi/4", "\pi/2"];
colors = {'b', 'r', [0 0.5 0]};
styles = {'-', '--', ':'};

fprintf('\n=== Point 7 ===\n');
fprintf('phi0 phidot0 phidot_c prediction simulation period\n');
fig = figure('Units', 'centimeters', 'Position', [2 2 17 7.5], 'Color', 'w');
try
    theme(fig, 'light');
end
hold on
for i = 1:3
    for j = 1:3
        p0 = phi0_list(i);
        pd0 = phidot0_list(j);
        [t7, X7] = ode45(@(t, X) diffeq(t, X, g, w, R, 0), 0:0.001:10, [p0; pd0], options);
        pdc = sqrt(2*g/R*(1 - sin(p0)));
        if pd0 > pdc
            pred = 'rotates';
        elseif pd0 == pdc
            pred = 'rest';
        else
            pred = 'oscillates';
        end
        Tosc = NaN;
        if max(abs(X7(:, 2))) < 1e-6
            sim_result = 'rest';
        elseif all(X7(:, 2) > 0)
            sim_result = 'rotates';
        else
            sim_result = 'oscillates';
            Tosc = mean(diff(t7(islocalmax(X7(:, 1)))));
        end
        fprintf('%.2f %.1f %.3f %s %s %.2f\n', p0, pd0, pdc, pred, sim_result, Tosc);
        % phi wrapped to one turn
        pw = mod(X7(:, 1) + 3*pi/2, 2*pi) - 3*pi/2;
        pw([false; abs(diff(pw)) > pi]) = NaN;
        plot(pw, X7(:, 2), styles{j}, 'Color', colors{i}, 'DisplayName', sprintf('$\\varphi_0=%s$, $\\dot\\varphi_0=%.1f$', phi_names(i), pd0))
        plot(p0, pd0, 'o', 'Color', colors{i}, 'MarkerFaceColor', colors{i}, 'HandleVisibility', 'off')
    end
end
ps = linspace(-3*pi/2, pi/2, 400);
plot(ps, sqrt(2*g/R*(1 - sin(ps))), 'k-.', 'DisplayName', 'separatrix')
plot(ps, -sqrt(2*g/R*(1 - sin(ps))), 'k-.', 'HandleVisibility', 'off')
plot(-pi/2, 0, 'k+', 'MarkerSize', 8, 'DisplayName', 'stable equilibrium')
xlabel('$\varphi$ (rad)'); ylabel('$\dot\varphi$ (rad/s)')
xlim([-3*pi/2 pi/2]); ylim([-8 8]); grid on
xticks(-3*pi/2:pi/2:pi/2); xticklabels({'$-3\pi/2$', '$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$'})
legend('Location', 'eastoutside', 'FontSize', 9)
exportgraphics(fig, 'figures/phase_portrait.png', 'Resolution', 300)

%% Point 8: linearized equation
A = 0.1;
R = 0.01;
wn = sqrt(g/R);
w_list = [1 1/2 1/4]*wn;
t8 = linspace(0, 10, 5001)';
col8 = [0 0 1; 1 0 0; 0 0.5 0];
light8 = 0.3*col8 + 0.7;
names = ["$\omega=\omega_n$", "$\omega=\omega_n/2$", "$\omega=\omega_n/4$"];

fprintf('\n=== Point 8 ===\n');
fprintf('omega_n = %.2f rad/s\n', wn);
fig = figure('Units', 'centimeters', 'Position', [2 2 17 6.5], 'Color', 'w');
try
    theme(fig, 'light');
end
for k = 1:3
    w = w_list(k);
    [~, Xf] = ode45(@(t, X) diffeq(t, X, g, w, R, A), t8, [-pi/2; 0], options);
    [~, Xl] = ode45(@(t, X) diffeqlin(t, X, g, w, R, A), t8, [0; 0], options);
    df = Xf(:, 1) + pi/2;
    dl = Xl(:, 1);
    err = 100*abs(dl - df)/max(abs(df));
    fprintf('omega = %.2f rad/s: max|delta| = %.3f rad = %.1f deg, max error = %.1f %%\n', w, max(abs(df)), max(abs(df))*180/pi, max(err));

    subplot(1, 2, 1)
    semilogy(t8, err, 'Color', light8(k, :), 'LineWidth', 0.5, 'HandleVisibility', 'off'); hold on
    semilogy(t8, movmax(err, 201), 'Color', col8(k, :), 'LineWidth', 1.5, 'DisplayName', names(k))
    if k == 2
        subplot(1, 2, 2)
        plot(t8, df, 'b', 'LineWidth', 0.5); hold on
        plot(t8, dl, 'r--', 'LineWidth', 0.5)
        xlabel('$t$ (s)'); ylabel('$\delta$ (rad)'); title('(b) $\omega=\omega_n/2$')
        legend('full', 'linearized', 'Location', 'north', 'Orientation', 'horizontal')
        xlim([0 10]); ylim([-0.25 0.35]); grid on
    end
end
subplot(1, 2, 1)
xlabel('$t$ (s)'); ylabel('Error (\%)'); title('(a)')
ylim([1e-3 100]); yticks([1e-3 1e-2 1e-1 1 10 100]); grid on
set(gca, 'YMinorGrid', 'off')
legend('Location', 'southeast')
exportgraphics(fig, 'figures/linearized_error.png', 'Resolution', 300)

%% Functions
function Xdot = diffeq(t, X, g, omega, R, A)
phi = X(1);
phidot = X(2);
Om = A*omega*sin(omega*t);
phiddot = -g/R*cos(phi) - Om^2*(1 + cos(phi))*sin(phi);
Xdot = [phidot; phiddot];
end

function Xdot = diffeqlin(t, X, g, omega, R, A)
delta = X(1);
deltadot = X(2);
Om = A*omega*sin(omega*t);
deltaddot = -g/R*delta + Om^2;
Xdot = [deltadot; deltaddot];
end
