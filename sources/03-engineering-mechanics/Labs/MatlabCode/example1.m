%% Example 1: Harmonic oscillator
clc
clear
close all
% Put your formatting options...
set ( groot , 'defaultAxesTickLabelInterpreter' , 'latex' ) ;
set ( groot , 'defaultTextInterpreter' , 'latex' ) ;
set(groot, 'defaultLineLineWidth', 2);
set(groot, 'defaultAxesFontSize', 12)
% etc....

% Harmonic oscillator
k = 25;            % spring's elastic constant   [kg/s^2]
m = 1;             % particle's mass [kg]
w = sqrt(k/m);     % system's frequency [1/s]
x_eq = .5;         % equilibrium position [m]
x0 = 2;            % initial position [m]
v0 = 0;            % initial velocity [m/s]
T = 2*pi/(w);      % period of oscillation
ICs = [x0;v0];     % initial condition column vector
dt = 0.01;         % timestep [s]
t_end = 2;         % final time [s]
timespan = 0:dt:t_end;     % time vector

% Analytical solution
x = @(t) x_eq + (x0-x_eq) * cos(w*t);

%Plot analytical solution
figure;
plot(timespan,   x(timespan), 'Color','blue', 'LineStyle','-')
xline(T, 'k--')
xlabel('$t$ [s]');
ylabel('$x$ [m]');
ylim([-2;5]);
title('Example 1');
grid on;
saveas(gcf,'ex_1_analytical', 'jpg')
%stop
%close

%% Numerical solution

% Integrate the ODE system and obtain the solution X
[tSol,stateSol] = ode45( @(t,X) diffeq(t,X,w,x_eq), [0;t_end], ICs);
% Obtain X from stateSol:
XSol = stateSol(:,1);
%Plot numerical solution
figure;
plot(tSol,XSol, 'Color','red', 'LineStyle','--')
xline(T,'k--')
xlabel('$t$ [s]');
ylabel('$x$ [m]');
% legend('numerical','analytical')
ylim([-2;5]);
title('Example 1');
grid on;
saveas(gcf,'ex_1_numerical.jpg', 'jpg')
% stop
% close

% Plot both together
figure;
plot(timespan,   x(timespan), 'Color','blue', 'LineStyle','-', 'DisplayName','Analytical')
hold on;
plot(tSol,XSol, 'Color','red', 'LineStyle','--', 'DisplayName','Numerical')
xlabel('$t$ [s]');
ylabel('$x$ [m]');
% legend('numerical','analytical')
ylim([-2;5]);
title('Example 1');
grid on;
legend('Interpreter', 'latex');
saveas(gcf,'ex_1_both.jpg', 'jpg')

%% Change the solver's tolerance

% change the options for the ODE solver
options1 = odeset('RelTol', 0.01, 'MaxStep', 2);

% Integrate the ODE system and obtain the solution X
[tSol,stateSol] = ode45(@(t,X) diffeq(t,X,w,x_eq),[0;t_end],ICs, options1);
% Obtain X from stateSol:
XSol = stateSol(:,1);
%Plot numerical solution
figure;
plot(tSol,XSol, 'Color','red','LineStyle','--')
xline(T,'k--')
xlabel('$t$ [s]');
ylabel('$x$ [m]');
% legend('numerical','analytical')
ylim([-2;5]);
title('Example 1');
grid on;
saveas(gcf,'ex_1_numerical_tol.jpg', 'jpg')
%stop
%close
% Plot both together
figure;
plot(timespan,   x(timespan), 'Color','blue', 'LineStyle','-', 'DisplayName','Analytical')
hold on;
plot(tSol,XSol, 'Color','red', 'LineStyle','--', 'DisplayName','Numerical')
xlabel('$t$ [s]');
ylabel('$x$ [m]');
% legend('numerical','analytical')
ylim([-2;5]);
title('Example 1');
grid on;
legend('Interpreter', 'latex');
saveas(gcf,'ex_1_both_tol.jpg', 'jpg')

%% STOP
% add the stopping event to the options
options2 = odeset(Events=@stopfun);

% Integrate the ODE system and obtain the solution X
[tSol,stateSol] = ode45(@(t,X) diffeq(t,X,w,x_eq),[0;t_end],ICs,options2);
% Obtain X from stateSol:
XSol = stateSol(:,1);
%Plot numerical solution
figure;
plot(tSol,XSol,'Color','red','LineStyle','--')
xline(T,'k--')
xlabel('$t$ [s]');
ylabel('$x$ [m]');
yline(0,'k--')
% legend('numerical','analytical')
ylim([-2;5]);
title('Example 1');
grid on;
saveas(gcf,'ex_1_numerical_event.jpg', 'jpg')
%stop
%close

%% Define Xdot = f(t,X,constants)
function Xdot=diffeq(t,X,w,x_eq)

Xdot = [X(2);-w^2*(X(1)-x_eq)];

end

%% Add a stop event when x=0
function [value,isterminal,direction] = stopfun(t,X)
value = X(1);
isterminal=1; % 1= halt integration
direction=-1;
end