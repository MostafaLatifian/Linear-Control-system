data = load('Data.mat');
freq =data.Data.omega;
mag = data.Data.magnitude;
phase =data.Data.phase;

phase = deg2rad(phase);
G = mag .* exp(1i * phase);
DataForresponse = frd(G , freq );
systemIdentification
