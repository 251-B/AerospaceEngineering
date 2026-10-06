%% Exercise 2: Parabolic motion
clc
clear
close all
% Put your formatting options...
set ( groot , 'defaultAxesTickLabelInterpreter' , 'latex' ) ;
set ( groot , 'defaultTextInterpreter' , 'latex' ) ;
set(groot, 'defaultLineLineWidth', 2);
set(groot, 'defaultAxesFontSize', 12)

% Parabolic motion
g = 9.81;                    % Acceleration due to gravity (m/s^2)
t_end = 2;                   % final time [s]
t = linspace(0, t_end, 100); % Time vector from 0 to 2 seconds
x0 = 1;                      % initial horizontal position [m]
y0 = 2;                      % initial vertical position [m]
alpha = pi/4;                % initial angle w.r.t. horizontal axis
v0 = 10;                     % initial velocity [m/s]
vx0 = v0 * cos(alpha);       % initial horizontal velocity
vy0 = v0 * sin(alpha);       % Initial vertical velocity
ICs = [x0;y0;vx0;vy0];       % initial conditions vector

% Analytical solution
x = x0 + vx0 * t;
y = y0 + vy0 * t -0.5 * g * t.^2;

% Plot the trajectory of the parabolic motion
figure;
plot(x, y);
xlabel('$x$ [m]');
ylabel('$y$ [m]');
ylim([-1,5]);
title('Example 2');
grid on;
saveas(gcf,'ex_2_analytical','jpg')
% close

%% Numerical solution

% Numerical integration for the complete state using ode45
[tSol, stateSol] = ode45(@(t,X) diffeq(t,X,g), [0;t_end], ICs);
% Extract positions from the state solution
xSol = stateSol(:, 1);
ySol = stateSol(:, 2);
vxSol = stateSol(:, 3);
vySol = stateSol(:, 4);

% Plot the numerical trajectory
figure;
plot(xSol, ySol,'Color','red','LineStyle','--');
xlabel('$x$ [m]');
ylabel('$y$ [m]');
ylim([-1,5]);
% legend('Numerical Trajectory', 'Analytical Trajectory');
title('Example 2');
grid on;
saveas(gcf, 'ex_2_comparison_trajectory.jpg');
% close

% Plot both together
figure;
plot(x, y, 'DisplayName','Analytical');
hold on;
plot(xSol, ySol,'Color','red','LineStyle','--', 'DisplayName','Numerical');
xlabel('$x$ [m]');
ylabel('$y$ [m]');
ylim([-1,5]);
% legend('Numerical Trajectory', 'Analytical Trajectory');
title('Example 2');
grid on;
legend('Interpreter', 'latex');
saveas(gcf, 'ex_2_both.jpg');
% close

%% Add a stop event when y=3 from any direction
options1 = odeset(Events=@stopfun);

% Numerical integration for the complete state using ode45
[tSol, stateSol] = ode45(@(t,X) diffeq(t,X,g), [0;t_end], ICs,options1);
% Extract positions from the state solution
xSol = stateSol(:, 1);
ySol = stateSol(:, 2);
vxSol = stateSol(:, 3);
vySol = stateSol(:, 4);

% Plot the numerical trajectory
figure;
plot(xSol, ySol,'Color','red','LineStyle','--');
xlabel('$x$ [m]');
ylabel('$y$ [m]');
ylim([-1,5]);
% legend('Numerical Trajectory', 'Analytical Trajectory');
title('Example 2');
grid on;
saveas(gcf, 'ex_2_comparison_stopfun1.jpg');
% stop
% close

%% Add a stop event when y=3 ONLY FROM ABOVE
options1 = odeset(Events=@stopfun1);

% Numerical integration for the complete state using ode45
[tSol, stateSol] = ode45(@(t,X) diffeq(t,X,g), [0;t_end], ICs,options1);
% Extract positions from the state solution
xSol = stateSol(:, 1);
ySol = stateSol(:, 2);
vxSol = stateSol(:, 3);
vySol = stateSol(:, 4);

% Plot the numerical trajectory
figure;
plot(xSol, ySol,'Color','red','LineStyle','--');
xlabel('$x$ [m]');
ylabel('$y$ [m]');
ylim([-1,5]);
% legend('Numerical Trajectory', 'Analytical Trajectory');
title('Example 2');
grid on;
saveas(gcf, 'ex_2_comparison_stopfun1.jpg');
% stop
% close

%% Functions
function Xdot= diffeq(t,X,g)

Xdot = [X(3);X(4);0;-g];

end

function [value,isterminal,direction] = stopfun1(t,X)
value = X(2) - 3;
isterminal = 1;
direction= -1;
end

function [value,isterminal,direction] = stopfun(t,X)
value = X(2) -3;
isterminal = 1;
direction= 0;
end