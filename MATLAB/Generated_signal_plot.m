% Loads in file from disk
file = uigetfile("*.mat");
load(file);

% Grab information from file
waveform = waveStruct.waveform;
Fs = waveStruct.Fs;

figure("Visible",true)
spectrogram(waveform);
% Removes axis and colorbar
set(gca, 'Visible', 'off');
colorbar('off');

% 
% %.Mat to .Wav might be usefull
% % https://www.mathworks.com/matlabcentral/answers/306487-convert-mat-files-to-wav
% 
% % Open .mat in python
% % https://www.mathworks.com/matlabcentral/answers/383427-proper-importing-of-matlab-structures-into-python