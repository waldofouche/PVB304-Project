% Loads in file from disk
addpath("mat", "spectrogram");
file = uigetfile("*.mat");
load(file);

% Grab information from file
waveform = waveStruct.waveform;
Fs = waveStruct.Fs;

figure("Visible",true)
spectrogram(waveform);
%shading interp;
%view(-45,65)
%colormap bone
title('5G Signal Spectrogram')
% Removes axis and colorbar
%set(gca, 'Visible', 'off');
%colorbar('off');

% c = parula * 255
% 
% %.Mat to .Wav might be usefull
% % https://www.mathworks.com/matlabcentral/answers/306487-convert-mat-files-to-wav
% 
% % Open .mat in python
% % https://www.mathworks.com/matlabcentral/answers/383427-proper-importing-of-matlab-structures-into-python