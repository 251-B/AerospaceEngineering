function [t_ball, x_ball, y_ball] = simulate_case4_ballistic(t0_ball, r0_ball, v0_ball, g, t_max)
% SIMULATE_CASE4_BALLISTIC Computes the unconstrained free-fall trajectory 
% of the particle after the string loses tension (T = 0).
%
% Inputs:
%   t0_ball : Time instant when tension vanishes [s]
%   r0_ball : [x0; y0] Position vector at tension loss [m]
%   v0_ball : [vx0; vy0] Velocity vector at tension loss [m/s]
%   g       : Gravity acceleration [m/s^2]
%   t_max   : Duration of ballistic flight simulation [s]
%
% Outputs:
%   t_ball  : Time vector [s]
%   x_ball  : Horizontal position [m]
%   y_ball  : Vertical position [m]

    dt = 0.001;
    t_ball = t0_ball : dt : (t0_ball + t_max);
    tau = t_ball - t0_ball;

    % Analytical ballistic parabolic equations (ax = 0, ay = -g)
    x_ball = r0_ball(1) + v0_ball(1) * tau;
    y_ball = r0_ball(2) + v0_ball(2) * tau - 0.5 * g * tau.^2;
end
