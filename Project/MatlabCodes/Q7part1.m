s = tf('s');
G = (0.1*s - 0.2) / (s * (s^2 + 0.9*s + 9));
k=-20;
C = k * (s + 0.1) / s;
L=C*G;
L2=L/s;
T = feedback(L, 1);
Kv = dcgain(s *L );
ess = 1 / Kv;  
fprintf('ثابت سرعت Kv: %.4f\n', Kv);
fprintf(' ess: %.4f ', ess);
figure;
step(L2);
figure;
margin(L)
pole(T)
