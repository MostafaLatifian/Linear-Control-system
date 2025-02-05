clc; clear all; close all;
s=tf('s');
G = (0.1*s - 0.2) / s/(s^2+0.9*s+9);
%% Root locus of system Q5
figure;
rlocus(G)
hold on;
rlocus(-G,' -. ')
 % sisotool(G,1)