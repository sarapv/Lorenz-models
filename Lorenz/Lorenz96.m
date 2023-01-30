clear
close all

%% stochastic Lorenz 96 parameters
F = 8;                  % forcing parameter
H = 0.75;               % coupling between slow and fast variables
C = 10;                 % time scale of variables y
B = 15;                 % inverse amplitude of the fast variables

h = 2e-4;               % integration period in natural units
t_final = 10;           % duration of the simulation in natural time units
NT = fix(t_final/h);    % no. of discrete time steps
nosc = 20;              % no. of oscillators
fps = 10;               % no. of fast variables per slow variable 
nosc_fast = fps*nosc;   % no. of fast variables
s2y = 4;                % variance of the observations: slow variables
s2u = 1/10;             % variance of the observations: fast variables
s2x = h/2;              % variance of the signal noise (slow variables)
s2z = h/8;              % variance of the signal noise (fast variables)
Tobs = 200;             % signals observed every Tobs time steps
% Oobs_x = 2;             % we observe one every Oobs_x slow oscillators
% Oobs_y = 5;             % we observe one every Oobs_y fast oscillators

% Initial conditions
x = zeros([nosc NT]);
x(1:nosc,1) = rand([nosc 1]);
z = zeros([nosc_fast NT]);
z(1:nosc_fast,1) = (1/(C*B))*rand([nosc_fast 1]) - 1/(2*C*B);

%% Euler integration
t0 = clock;
ok = 0;
while not(ok)
    for n = 2:NT

        % slow variables
        x(1,n) = x(1,n-1) + h*( -x(nosc,n-1)*(x(nosc-1,n-1) - x(2,n-1)) - x(1,n-1) + F - ((H*C)/B)*sum(z(1:fps,n-1)) ) + sqrt(s2x)*randn;
        x(2,n) = x(2,n-1) + h*( -x(1,n-1)*(x(nosc,n-1) - x(3,n-1)) - x(2,n-1) + F - ((H*C)/B)*sum(z(fps+(1:fps),n-1)) ) + sqrt(s2x)*randn;

        for i=3:nosc-1
            x(i,n) = x(i,n-1) + h*( -x(i-1,n-1)*(x(i-2,n-1) - x(i+1,n-1)) - x(i,n-1) + F - ((H*C)/B)*sum(z((i-1)*fps+(1:fps),n-1)) ) + sqrt(s2x)*randn;
        end %i
        x(nosc,n) = x(nosc,n-1) + h*( -x(nosc-1,n-1)*(x(nosc-2,n-1) - x(1,n-1)) - x(nosc,n-1) + F - ((H*C)/B)*sum(z((nosc-1)*fps+(1:fps),n-1)) ) + sqrt(s2x)*randn;

        
        % fast variables
        id_x = 1;
        z(1,n) = z(1,n-1) + h*( C*B*z(2,n-1)*(z(nosc_fast,n-1) - z(3,n-1)) - C*z(1,n-1) + F*C/B + (C*H/B)*x(id_x,n-1) ) + sqrt(s2z)*randn;

        for j = 2:nosc_fast-2
            id_x = 1 + floor(j/fps);
            z(j,n) = z(j,n-1) + h*( C*B*z(j+1,n-1)*(z(j-1,n-1) - z(j+2,n-1)) - C*z(j,n-1) + F*C/B + (C*H/B)*x(id_x,n-1) ) + sqrt(s2z)*randn;
        end %j
        
        id_x = nosc;
        z(nosc_fast-1,n) = z(nosc_fast-1,n-1) + h*( C*B*z(nosc_fast,n-1)*(z(nosc_fast-2,n-1) - C*z(1,n-1)) - z(nosc_fast-1,n-1) + F*C/B + (C*H/B)*x(id_x,n-1) ) + sqrt(s2z)*randn;
        z(nosc_fast,n) = z(nosc_fast,n-1) + h*( C*B*z(1,n-1)*(z(nosc_fast-1,n-1) - z(2,n-1)) - C*z(nosc_fast,n-1) + F*C/B + (C*H/B)*x(id_x,n-1) ) + sqrt(s2z)*randn;

    end %n
    
    
    ok = isempty( find( isnan(x(1,:)) | isinf(x(1,:)), 1 ) );   %Check wheter the integration have worked or not
    
    
end %while

% Observations
y = x + sqrt(s2y)*randn(size(x));   % for the slow variables
u = z + sqrt(s2u)*randn(size(z));   % for the fast variables

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
