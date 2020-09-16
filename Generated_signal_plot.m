% Loads in file from disk
file = uigetfile("*.mat");
load(file);

% Grab information from file
Fs = waveStruct.Fs; % Sampling Frequency
waveform = waveStruct.waveform;

% Plot
% Time Scope
timeScope = dsp.TimeScope('SampleRate', Fs, ...
    'TimeSpanOverrunAction', 'Scroll', ...
    'TimeSpan', 7.8125e-06);
timeScope(waveform);
release(timeScope)

% Spectrum Analyzer
spectrum = dsp.SpectrumAnalyzer('SampleRate', Fs);
spectrum(waveform);
release(spectrum);

%.Mat to .Wav might be usefull
% https://www.mathworks.com/matlabcentral/answers/306487-convert-mat-files-to-wav