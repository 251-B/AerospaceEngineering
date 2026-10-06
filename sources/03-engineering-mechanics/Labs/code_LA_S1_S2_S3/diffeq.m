function Xdot = diffeq(t, X, g, a, omega, xi0)
% DIFFEQ Evaluates the first-order state-space derivatives for the 
% particle connected to a rotating spool.
%
% State vector:
%   X(1) = phi      [rad]   (angular position of spool tangency point B)
%   X(2) = phi_dot  [rad/s] (angular velocity of B)
%
% Output:
%   Xdot = [phi_dot; phi_ddot]

    phi     = X(1);
    phi_dot = X(2);

    % Unspooled string length at current time and configuration
    xi = xi0 + a * (phi - omega * t);

    % Guard against division by non-positive length (singularity at xi -> 0)
    if xi <= 1e-7
        xi = 1e-7;
    end

    % Angular acceleration derived from normal projection (orthogonal to tension)
    % m * (xi * phi_ddot + a * phi_dot^2 - 2 * a * omega * phi_dot) = -m * g * sin(phi)
    phi_ddot = (-g * sin(phi) - a * phi_dot^2 + 2 * a * omega * phi_dot) / xi;

    Xdot = [phi_dot; phi_ddot];
end
