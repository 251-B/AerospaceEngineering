% Physical parameters
g = 9.81;
m = 0.1;
a = 0.2;
phi0 = 0;
xi0 = 1;

% Study cases: [omega, v0]
cases = [ ...
    0.1,   0.0;
    0.0,  -1.0;
    0.0, -10.0;
    0.0,   4.0;
    0.1,   1.0];

for k = 1:size(cases, 1)
    omega = cases(k, 1);
    v0 = cases(k, 2);
    phidot0 = v0 / xi0;
    tspan = [0, 20];
    X0 = [phi0; phidot0];
    
    options = odeset('Events', @(t, X) stopfun(t, X, g, omega, a, xi0, m), ...
        'RelTol', 1e-8, 'AbsTol', 1e-8);
        
    [t, X] = ode45(@(t, X) diffeq(t, X, g, omega, a, xi0), tspan, X0, options);
    
    phi = X(:, 1);
    phidot = X(:, 2);
    xi = xi0 - a * (omega * t - phi);
    T = m * xi .* phidot.^2 + m * g * cos(phi);
    x = a * cos(phi) + xi .* sin(phi);
    y = a * sin(phi) - xi .* cos(phi);
    E = 0.5 * m * (xi.^2 .* phidot.^2 + a^2 * omega^2) + m * g * y;
    
    figure('Name', sprintf('Case %d', k), 'NumberTitle', 'off');
    
    % Subplot 1: State Variables
    subplot(2, 2, 1);
    plot(t, phi, 'b', 'LineWidth', 1.5); hold on;
    plot(t, xi, 'r', 'LineWidth', 1.5);
    xlabel('t (s)');
    ylabel('State variables');
    legend('\phi (rad)', '\xi (m)', 'Location', 'best');
    grid on;
    title(sprintf('Case %d: State Variables', k));
    
    % Subplot 2: String Tension
    subplot(2, 2, 2);
    plot(t, T, 'k', 'LineWidth', 1.5);
    xlabel('t (s)');
    ylabel('T (N)');
    grid on;
    title(sprintf('Case %d: String Tension', k));
    
    % Subplot 3: Spatial Trajectory
    subplot(2, 2, 3);
    plot(x, y, 'b', 'LineWidth', 1.5); hold on;
    theta_circle = linspace(0, 2*pi, 300);
    plot(a * cos(theta_circle), a * sin(theta_circle), '--r', 'LineWidth', 1.5);
    xlabel('x (m)');
    ylabel('y (m)');
    axis equal;
    grid on;
    title(sprintf('Case %d: Spatial Trajectory', k));
    
    % Subplot 4: Total Mechanical Energy
    subplot(2, 2, 4);
    plot(t, E, 'm', 'LineWidth', 1.5);
    xlabel('t (s)');
    ylabel('E (J)');
    grid on;
    title(sprintf('Case %d: Total Mechanical Energy', k));
    
    saveas(gcf, sprintf('Case%d_results.png', k));
end

% --- Differential Equation Function ---
function Xdot = diffeq(t, X, g, omega, a, xi0)
    phi = X(1);
    phidot = X(2);
    xi = xi0 - a * (omega * t - phi);
    phiddot = (-g * sin(phi) - a * phidot^2 + 2 * a * omega * phidot) / xi;
    Xdot = [phidot; phiddot];
end

% --- Event Function ---
function [value, isterminal, direction] = stopfun(t, X, g, omega, a, xi0, m)
    phi = X(1);
    phidot = X(2);
    xi = xi0 - a * (omega * t - phi);
    T = m * xi * phidot^2 + m * g * cos(phi);
    
    value = [xi; T];       % Detect when xi or T reaches 0
    isterminal = [1; 1];   % Stop the integration
    direction = [-1; -1];  % Only detect when they are decreasing
end