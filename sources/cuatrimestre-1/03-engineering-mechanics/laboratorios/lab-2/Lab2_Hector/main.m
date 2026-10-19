%% Lab 2 - Particle on oscillating loop
% Mechanics Applied to Aerospace Engineering (UC3M)
% Group LA: Alvarez Iglesias, Gonzalez Rodriguez, Hernandez Bejarano
clear; clc; close all;

% use LaTeX in the labels of the plots
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');

%% Data of the problem
g    = 9.81;   % gravity (m/s^2)
m    = 1;      % mass of the particle (kg)
R    = 1;      % radius of the wire (m)
A    = pi;     % amplitude of the rotation angle (rad)
w    = 0.1;    % frequency of the loop oscillation (rad/s)
phi0  = 0;     % initial angle (rad)
dphi0 = 0;     % initial angular rate (rad/s)
Tper = 2*pi/w; % period of the rotating reference system (s)

%% Items 5 and 6: integration for t = [0, 3T]
% state X = [phi; dphi]
options = odeset('RelTol', 1e-8, 'AbsTol', 1e-10);
[t, stateSol] = ode45(@(t,X) diffeq(t, X, g, R, A, w), linspace(0, 3*Tper, 3000), [phi0; dphi0], options);

phi  = stateSol(:,1);
dphi = stateSol(:,2);

Om    = A*w*sin(w*t);     % angular rate of the loop
Omdot = A*w^2*cos(w*t);   % angular acceleration of the loop
x     = R*(1 + cos(phi)); % distance of P to the axis of rotation
y     = R*sin(phi);

% reaction forces (Nr: radial, in the plane of the loop; Nz: perpendicular to it)
% inertia forces in the rotating frame (centrifugal along x, Coriolis and Euler along z)
Fcf  = m*Om.^2.*x;
Fcor = -2*m*Om.*R.*dphi.*sin(phi);
Feul = m*Omdot.*x;
Nr   = -m*R*dphi.^2 + m*g*sin(phi) - Fcf.*cos(phi);
Nz   = -(Fcor + Feul);

% energies (kinetic energy with respect to the fixed frame)
Ek = 0.5*m*(R^2*dphi.^2 + Om.^2.*x.^2);
Ep = m*g*y;

% position of P in the fixed frame Ox1y1z1
theta = A*(1 - cos(w*t));   % rotation angle of the loop
x1 = x.*cos(theta);
y1 = y;
z1 = -x.*sin(theta);

%% Figure 1: phi, forces and energies
figure(1)
subplot(2,2,1)
plot(t, phi, 'b'); grid on
xlabel('$t$ (s)'); ylabel('$\varphi$ (rad)'); title('(a) Angle')

subplot(2,2,2)
plot(t, Nr, 'b', t, Nz, 'r--'); grid on
xlabel('$t$ (s)'); ylabel('reaction (N)'); title('(b) Reaction forces')
legend('$N_r$', '$N_z$')

subplot(2,2,3)
plot(t, Fcf, 'b', t, Fcor, 'r--', t, Feul, 'm-.'); grid on
xlabel('$t$ (s)'); ylabel('inertia force (N)'); title('(c) Inertia forces')
legend('centrifugal', 'Coriolis', 'Euler')

subplot(2,2,4)
plot(t, Ek, 'b', t, Ep, 'r--', t, Ek+Ep, 'k:'); grid on
xlabel('$t$ (s)'); ylabel('energy (J)'); title('(d) Energies')
legend('$E_k$', '$E_p$', '$E_k + E_p$')

%% Figure 2: trajectory of P in the fixed frame
figure(2)
plot3(x1, z1, y1, 'b'); hold on
plot3(x1(1), z1(1), y1(1), 'ko', 'MarkerFaceColor', 'k')   % start
plot3(x1(end), z1(end), y1(end), 'rx', 'LineWidth', 2)     % end
axis equal; grid on
xlabel('$x_1$ (m)'); ylabel('$z_1$ (m)'); zlabel('$y_1$ (m)')
title('Trajectory of P in the fixed frame')
legend('trajectory of P', '$t = 0$', '$t = 3T$')
view(30, 25)

%% Item 7: A = 0, phase portrait for the nine initial conditions
phi0v  = [0 pi/4 pi/2];
dphi0v = [0 1.5 3];
colors = {'b', 'r', 'm'};
styles = {'-', '--', ':'};
tend7  = 3;

figure(3)
hold on
pmax = 0;
for i = 1:3
    for j = 1:3
        [t7, S7] = ode45(@(t,X) diffeq(t, X, g, R, 0, w), [0 tend7], [phi0v(i); dphi0v(j)], options);
        plot(S7(:,1), S7(:,2), [colors{i} styles{j}])
        names{3*(i-1)+j} = ['$\varphi_0 = ' num2str(phi0v(i), '%.2f') '$, $\dot\varphi_0 = ' num2str(dphi0v(j)) '$'];
        pmax = max(pmax, max(S7(:,1)));

        % critical rate from the energy: E = (1/2)R^2 dphi^2 + g R sin(phi) > g R
        dcrit = sqrt(2*g/R*(1 - sin(phi0v(i))));
        if dphi0v(j) > dcrit
            fprintf('phi0 = %.2f, dphi0 = %.1f (critical %.3f): phi increases steadily\n', phi0v(i), dphi0v(j), dcrit);
        else
            fprintf('phi0 = %.2f, dphi0 = %.1f (critical %.3f): phi oscillates\n', phi0v(i), dphi0v(j), dcrit);
        end
    end
end
pp = linspace(-pi, pmax, 500);
plot(pp, sqrt(2*g/R*(1 - sin(pp))), 'k-.', 'LineWidth', 1.5)   % separatrix
grid on
xlabel('$\varphi$ (rad)'); ylabel('$\dot\varphi$ (rad/s)'); title('Phase portrait ($A = 0$)')
legend([names {'separatrix'}], 'Location', 'eastoutside')

%% Item 8: linearized equation, A^2 << g/(R w^2)
Rs     = 0.01;                  % radius of the wire (m)
As     = 0.1;                   % amplitude (rad)
ws     = sqrt(g/Rs)*[1 1/2 1/4];
delta0 = 0.01;                  % initial delta (rad)
tend8  = 10;

figure(4)
for k = 1:3
    % full equation (phi = delta - pi/2) and linearized equation
    [t8, Sfull] = ode45(@(t,X) diffeq(t, X, g, Rs, As, ws(k)), linspace(0, tend8, 2000), [-pi/2 + delta0; 0], options);
    [~,  Slin]  = ode45(@(t,X) diffeqlin(t, X, g, Rs, As, ws(k)), linspace(0, tend8, 2000), [delta0; 0], options);

    dfull = Sfull(:,1) + pi/2;
    dlin  = Slin(:,1);
    err   = 100*abs(dlin - dfull)./max(abs(dfull));   % percentage error (relative to the amplitude of delta)

    semilogy(t8, err + eps); hold on
end
grid on
xlabel('$t$ (s)'); ylabel('error (\%)'); title('Linearized vs full equation')
legend('$\omega = \sqrt{g/R}$', '$\omega = (1/2)\sqrt{g/R}$', '$\omega = (1/4)\sqrt{g/R}$', 'Location', 'northwest')

%% Functions
function Xdot = diffeq(t, X, g, R, A, w)
    phi  = X(1);
    dphi = X(2);
    Om   = A*w*sin(w*t);                                          % angular rate of the loop
    ddphi = -g/R*cos(phi) - Om^2*(1 + cos(phi))*sin(phi);         % equation of motion
    Xdot = [dphi; ddphi];
end

function Xdot = diffeqlin(t, X, g, R, A, w)
    delta  = X(1);
    ddelta = X(2);
    Om = A*w*sin(w*t);
    Xdot = [ddelta; -g/R*delta + Om^2];                           % linearized equation
end
