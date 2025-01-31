clc; clear; close
s = tf('s');
G_without_delay = 1/((s)*(s+1)*(s^2+4*s+8));
subplot(2,1,1)
rlocus(G_without_delay);
title('System Without Delay');
G_with_delay = (1-s)/((s)*((s+1)^2)*(s^2+4*s+8));
subplot(2,1,2)
rlocus(G_with_delay);
title('System With Delay');