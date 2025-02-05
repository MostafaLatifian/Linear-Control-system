clc; clear; close all;
%% bode plot of system Q1
data = load('Data.mat');
freq = data.Data.omega;    
mag = data.Data.magnitude;  
phase = data.Data.phase; 
s=tf('s');
figure;
subplot(2,1,1);
semilogx(freq, 20*log10(mag));
grid on;
xlabel('Frequency');
ylabel('Magnitude');
title('Bode Magnitude');

subplot(2,1,2);
semilogx(freq, phase);
grid on;
xlabel('Frequency');
ylabel('Phase');
title('Bode Phase');

%% Find transfer function of system Q3
% P = deg2rad(phase);
% L = mag .*exp(1i*P);
% Connectform=0;
% freq_store=idfrd(L,freq,Connectform);
% p=3;
% z=1;
% G = tfest(freq_store,p,z);
% G
% figure;
% bode(G);
% grid on;
G = (0.1*s - 0.2) / s/(s^2+0.9*s+9);
%% Root locus of system Q5
figure;
rlocus(G)
figure;
rlocus(-G)
%% Mp and ts Q6
G2=(0.1)/(s^2+0.9*s+9);
figure;
margin(G2) %G2 befor lead controller

C_lead=(0.1*(0.34*s+1))/(0.25*s+1);
% figure;
% margin(G2 * C_lead)  % G2 after lead controller
% figure;
% step(G2 * C_lead)
% info = stepinfo(G2*C_lead);    % Get step response characteristics
% overshoot = info.Overshoot     % Overshoot percentage
% settling_time = info.SettlingTime % Settling time
% figure;
% margin(G2*C_lead) % G2 before lag
C_lag=(1.6*(1.9*s+1))/(3.13*s+1);
figure;
margin(G2 * C_lead*C_lag) % G2 after both
T2=G2 *C_lead*C_lag;
T3=(T2)/(T2+1);
figure;
step(T3)
figure;
step(G2)
info = stepinfo(T3);
overshoot = info.Overshoot    
settling_time = info.SettlingTime