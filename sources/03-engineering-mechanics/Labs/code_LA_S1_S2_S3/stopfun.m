function [value, isterminal, direction] = stopfun(t, X, g, m, a, omega, xi0)
% STOPFUN Event function for ODE45 to detect critical physical terminations:
%   Event 1: Particle hits the spool surface (xi = 0)
%   Event 2: String loses tension / becomes slack (T = 0)
%
% Output arguments:
%   value      : Vector [xi; T] of event conditions to monitor
%   isterminal : [1; 1] halts the numerical integration when either condition occurs
%   direction  : [-1; -1] triggers only when crossing zero from positive to negative

    phi     = X(1);
    phi_dot = X(2);

    % Current unspooled straight string length
    xi = xi0 + a * (phi - omega * t);

    % String tension from radial/tangential Newton-Euler projection:
    % T = m * (xi * phi_dot^2 + g * cos(phi))
    T = m * (xi * phi_dot^2 + g * cos(phi));

    % Physical contact threshold: the particle hits the spool surface when xi -> 0.
    % To prevent ODE45 step-size collapse at the exact algebraic singularity (xi=0, ddot(phi)->inf),
    % collision is detected when the unspooled length reaches the threshold eps_contact.
    eps_contact = 1e-3; % 1 mm from spool surface
    
    % We monitor xi reaching eps_contact (hitting spool) and T reaching 0 (slacking)
    value      = [xi - eps_contact; T];
    isterminal = [1; 1];
    direction  = [-1; -1];
end
