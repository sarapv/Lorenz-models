clear
close all

%% stochastic Lorenz 96 parameters
F = 8;                  % forcing parameter
h = 2e-4;               % integration period in natural units
t_final = 10;           % duration of the simulation in natural time units
NT = fix(t_final/h);    % no. of discrete time steps
nosc = 20;              % no. of oscillators
s2y = 4;                % variance of the observations
s2x = 1/2;              % variance of the signal noise
Tobs = 200;             % signals observed every Tobs time steps

% Initial conditions
x = zeros([nosc NT]);
x(1:nosc,1) = rand([nosc 1]);

%% Euler integration
t0 = clock;
ok = 0;
while not(ok)
    for n = 2:NT

        % slow variables
        x(1,n) = x(1,n-1) + h*( -x(nosc,n-1)*(x(nosc-1,n-1) - x(2,n-1)) - x(1,n-1) + F ) + sqrt(h*s2x)*randn;
        x(2,n) = x(2,n-1) + h*( -x(1,n-1)*(x(nosc,n-1) - x(3,n-1)) - x(2,n-1) + F ) + sqrt(h*s2x)*randn;

        for i=3:nosc-1
            x(i,n) = x(i,n-1) + h*( -x(i-1,n-1)*(x(i-2,n-1) - x(i+1,n-1)) - x(i,n-1) + F ) + sqrt(h*s2x)*randn;
        end %i
        x(nosc,n) = x(nosc,n-1) + h*( -x(nosc-1,n-1)*(x(nosc-2,n-1) - x(1,n-1)) - x(nosc,n-1) + F ) + sqrt(h*s2x)*randn;


    end %n


    ok = isempty( find( isnan(x(1,:)) | isinf(x(1,:)), 1 ) );   %Check wheter the integration have worked or not


end %while

% Observations
y = x + sqrt(s2y)*randn(size(x));

%% Figures

figure(1),
idx_plotted = 1:2;
for i = idx_plotted
    subplot(length(idx_plotted),1,i),
    plot(1:NT,x(i,:),'k'), hold on,
    plot(1:Tobs:NT,y(i,1:Tobs:end),'*')
end
legend('state','observations')
% sgtitle('State and observations')
