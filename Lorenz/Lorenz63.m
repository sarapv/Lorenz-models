clear
close all

%% Stochastic Lorenz 63 model

% Parameters
s = 10;
r = 28; 
b = 8/3; 

h=1e-3;     %time (integration) step
T = 20000;  % total number of time steps
Tobs = 40;  % steps/time between observations

s2x = h/2;  % variance of the state noise
s2y = 1;    % variance of the observation noise

dx = 3;     % dimension of the state
dy = 3;     % dimension of the observation

idx_observed = 1:3; % which states are 'observed'


x = zeros(3,T);
y = zeros(length(idx_observed),T);

% initialization
x(:,1)=sqrt(s2x)*randn(dx,1);
y(:,1)=x(idx_observed,1)+sqrt(s2y)*randn(dy,1);


% Generating ground truth / synthetic data
for t = 2:T
   x(1,t) = x(1,t-1) + h * ( -s * (x(1,t-1) - x(2,t-1)) ) + sqrt(s2x)*randn ;
   x(2,t) = x(2,t-1) + h * (r*x(1,t-1) - x(2,t-1) - (x(1,t-1)*x(3,t-1)) ) + sqrt(s2x)*randn ;
   x(3,t) = x(3,t-1) + h * ( (-b * x(3,t-1)) + (x(1,t-1)*x(2,t-1)) ) + sqrt(s2x)*randn ;
   
   if mod(t,Tobs)==1
      y(:,t)=x(idx_observed,t)+sqrt(s2y)*randn(dy,1); 
   end
   
end

%% Figures
figure(1),
for i = idx_observed
    subplot(length(idx_observed),1,i),
    plot(1:T,x(i,:),'k'), hold on, 
    plot(1:Tobs:T,y(i,1:Tobs:end),'*')
end
legend('state','observations')
% sgtitle('State and observations')

figure(2)
subplot(311),
plot(x(1,:),x(2,:)), title('XY plane')

subplot(312),
plot(x(1,:),x(3,:)), title('XZ plane')

subplot(313),
plot(x(2,:),x(3,:)), title('YZ plane')