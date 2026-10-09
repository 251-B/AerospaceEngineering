%% Lab 1 - Particle connected to a spool
% Mechanics Applied to Aerospace Engineering (UC3M)
% Group LA: Alvarez Iglesias, Gonzalez Rodriguez, Hernandez Bejarano
clear; clc; close all;
warning('off', 'MATLAB:ode45:IntegrationTolNotMet');

% use LaTeX in the labels of the plots
set(groot, 'defaultTextInterpreter', 'latex');
set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
set(groot, 'defaultLegendInterpreter', 'latex');

%% Data of the problem
g    = 9.81;   % gravity (m/s^2)
m    = 0.1;    % mass of the particle (kg)
a    = 0.2;    % radius of the spool (m)
xi0  = 1;      % initial free length of the string (m)
phi0 = 0;      % initial angle (rad)

% each row is one case: omega (rad/s), vx(0) (m/s), final time (s)
cases = [0.1    0   55;
         0     -1   20;
         0    -10  0.5;
         0      4    2;
         0.1    1   40];

%% Solve the 5 cases with ode45
for k = 1:5
    w    = cases(k,1);
    vx0  = cases(k,2);
    tend = cases(k,3);

    % state X = [phi; dphi; W], W is the work done by the spool
    ICs = [phi0; vx0/xi0; 0];

    options = odeset('RelTol', 1e-8, 'AbsTol', 1e-10, ...
                     'Events', @(t,X) stopfun(t, X, g, w, a, m, xi0));
    [tSol, stateSol] = ode45(@(t,X) diffeq(t, X, g, w, a, m, xi0), [0 tend], ICs, options);

    % save the results of this case
    t{k}    = tSol;
    phi{k}  = stateSol(:,1);
    dphi{k} = stateSol(:,2);
    W{k}    = stateSol(:,3);
    xi{k}   = xi0 + a*(phi{k} - w*tSol);
    T{k}    = m*(g*cos(phi{k}) + max(xi{k},0).*dphi{k}.^2);
    x{k}    = a*cos(phi{k}) + xi{k}.*sin(phi{k});
    y{k}    = a*sin(phi{k}) - xi{k}.*cos(phi{k});
    E{k}    = 0.5*m*(xi{k}.^2.*dphi{k}.^2 + a^2*w^2) + m*g*y{k};

    fprintf('Case %d: integration stops at t = %.4f s\n', k, tSol(end));
end

%% Figure 1: phi, xi and T for each case
figure(1)
for k = 1:5
    subplot(5,3,3*k-2)
    plot(t{k}, phi{k}, 'b'); grid on
    xlabel('$t$ (s)'); ylabel('$\phi$ (rad)'); title(['Case ' num2str(k)])

    subplot(5,3,3*k-1)
    plot(t{k}, xi{k}, 'b'); grid on
    xlabel('$t$ (s)'); ylabel('$\xi$ (m)'); title(['Case ' num2str(k)])

    subplot(5,3,3*k)
    if k == 3 || k == 5
        semilogy(t{k}, T{k}, 'b')   % T becomes very large at the end
    else
        plot(t{k}, T{k}, 'b')
    end
    grid on
    xlabel('$t$ (s)'); ylabel('$T$ (N)'); title(['Case ' num2str(k)])
end

%% Figure 2: trajectory of P
figure(2)
th = linspace(0, 2*pi, 200);
for k = 1:5
    subplot(2,3,k)
    hold on
    fill(a*cos(th), a*sin(th), [0.85 0.85 0.85])          % spool
    plot(x{k}, y{k}, 'b')                                  % trajectory
    plot(x{k}(1), y{k}(1), 'ko', 'MarkerFaceColor', 'k')   % start
    plot(x{k}(end), y{k}(end), 'rx', 'LineWidth', 2)       % end
    axis equal; grid on
    xlabel('$x$ (m)'); ylabel('$y$ (m)'); title(['Case ' num2str(k)])
end
legend('spool', 'trajectory of P', '$t = 0$', 'end of integration', ...
       'Position', [0.72 0.25 0.15 0.15])

%% Figure 3: mechanical energy
figure(3)
for k = 1:5
    subplot(2,3,k)
    plot(t{k}, E{k}, 'b'); grid on
    xlabel('$t$ (s)'); ylabel('$E$ (J)'); title(['Case ' num2str(k)])
    if cases(k,1) == 0
        ylim([E{k}(1)-0.5, E{k}(1)+0.5])   % same scale for the cases with omega = 0
    end
end
% relative change of E when omega = 0 (should be almost zero)
subplot(2,3,6)
semilogy(t{2}, abs(E{2}-E{2}(1))/abs(E{2}(1)) + eps, 'b', ...
         t{3}, abs(E{3}-E{3}(1))/abs(E{3}(1)) + eps, 'r--', ...
         t{4}, abs(E{4}-E{4}(1))/abs(E{4}(1)) + eps, 'm-.')
grid on
xlabel('$t$ (s)'); ylabel('$|E-E_0|/|E_0|$'); title('Numerical error ($\omega = 0$)')
legend('Case 2', 'Case 3', 'Case 4')

%% Figure 4: end of Case 3 and energy balance of Case 5
figure(4)
subplot(1,2,1)
tf = t{3}(end);
v  = sqrt(cases(3,2)^2 - 2*g*(y{3}(end) - y{3}(1)));   % speed at the hit (energy conservation)
dt = tf - t{3}(1:end-1);
loglog(dt, abs(dphi{3}(1:end-1)), 'b', dt, sqrt(v./(2*a*dt)), 'r--'); grid on
xlabel('$t_f - t$ (s)'); ylabel('$|\dot\phi|$ (rad/s)'); title('(a) Case 3')
legend('numerical', '$\propto (t_f-t)^{-1/2}$')

subplot(1,2,2)
plot(t{5}, E{5}-E{5}(1), 'b', t{5}, W{5}, 'r--'); grid on
xlabel('$t$ (s)'); ylabel('energy (J)'); title('(b) Case 5')
legend('$E - E_0$', '$\int a\omega T\,dt$', 'Location', 'northwest')

%% Functions
function Xdot = diffeq(t, X, g, w, a, m, xi0)
    phi  = X(1);
    dphi = X(2);
    xi   = xi0 + a*(phi - w*t);                          % free length of the string
    ddphi = (-g*sin(phi) - a*dphi^2 + 2*a*w*dphi) / xi;  % equation of motion
    T = m*(g*cos(phi) + xi*dphi^2);                      % tension
    Xdot = [dphi; ddphi; a*w*T];                         % dW/dt = a*w*T
end

function [value, isterminal, direction] = stopfun(t, X, g, w, a, m, xi0)
    phi  = X(1);
    dphi = X(2);
    xi = xi0 + a*(phi - w*t);
    T  = m*(g*cos(phi) + max(xi,0)*dphi^2);
    value      = [xi; T];     % stop if the string is finished or if T = 0
    isterminal = [1; 1];
    direction  = [-1; -1];
end
