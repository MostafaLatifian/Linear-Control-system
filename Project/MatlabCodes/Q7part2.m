clc; clear all; close all;

s=tf('s');
G = (0.1*s-0.2)/(s^3+0.9*s^2+9*s);
Td=(-0.5*(s-2))/((s+1)^3);
Sd=(s^3+3*s^2+3.5*s)/((s+1)^3);
C=Td/(Sd*G);
LoopGain = 1.195*C*G;
CloseLoop = feedback(LoopGain,1);

figure;
step(CloseLoop)
info = stepinfo(CloseLoop);
Undershoot = info.Undershoot;
settling_time = info.SettlingTime; 

CloseLoop2=CloseLoop/s;
figure;
step(CloseLoop2)
title('ramp response')