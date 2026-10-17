clear all
close all
clc

%% Initialise simulation variables
U = 1;        
alpha = 1;
k = 0.5;
tmax = 20;                      % Maximum simulation time
% Boundary condition: choose from 'Dirichlet', 'Neumann' and 'Periodic'
BC = 'Dirichlet';               

Nx = 201;                         % Grid size (number of points)
Dx = 20/(Nx-1);               % Spacing between points

% Maximum timestep that satisfies stability conditions
Dt1 = 0.5*Dx/U;
Dt2 = 0.5*Dx^2/alpha;

Dt = min([Dt1, Dt2]);                 % Timestep 

x = -10:Dx:10;                      % Space array (contains position of grid points)
t = 0:Dt:tmax;                      % Time array (from 0 to tmax)
Nt = length(t);                     

% Initialise f
f = zeros(Nx, Nt);                  
f(:,1) = sech(k*(x+2)).^2;        

%% Finite differences simulation 
for n = 1:Nt-1
    
    % Inner points (from i = 2 to i = Nx-1)
    for i = 2:Nx-1
        f(i,n+1) = f(i,n);  % INCOMPLETE! EDIT ACCORDING TO EQ (10)

    end
    
    % Points at boundary (at i = 1 and i = Nx)
    switch BC
            case 'Dirichlet'               
            % Dirichlet Boundary Conditions
                f(1,n+1) = 0.0;
                f(Nx,n+1) = 0.0;                   
    
            case 'Neumann'
            % Neumann Boundary Condtions
                % f(1,n+1) =  ....    % EDIT
                % f(Nx,n+1) = ....  % EDIT
  
             
            case 'Periodic'
            % Periodic Boundary Conditions
               % f(1,n+1) =  ....    % EDIT
               % f(Nx,n+1) = ....  % EDIT
                    
            otherwise
                return   
                
    end 
end

%% Plot dynamic graph
% Initialise plot
fig=figure(1); 
clf
axfig = gca;
axfig.FontSize = 16;
hold on
box on
grid on
axfig.XLim = [-10 10];
axfig.YLim = [-0.5 1.0];
axfig.TickLabelInterpreter = 'latex';
xlabel('$x$', 'Interpreter', 'latex');
ylabel('$f$', 'Interpreter', 'latex', 'rotation', 0);
p = plot(0,0);      % Dummy plot (gets deleted afterwards)

% Plot curves
for n = 1:30:Nt
    delete(p);                                                                                           % Delete previous curve
    p = plot(x, f(:,n), '.k-');                                                                       %  Plot the wave
    title(['$t = \ $'  num2str(t(n), '%2.2f')] , 'Interpreter', 'latex')        % Update title with the time
    pause(0.1)                                                                                          % Pause time (secs) between consecutive graphs
end

%% Plot graph for report (COMPLETE)

