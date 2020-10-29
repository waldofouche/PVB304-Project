
path = 'C:\Users\Waldo\Documents\GitHub\PVB304-Project\MATLAB';
figuresdir = 'C:\Users\Waldo\Documents\GitHub\PVB304-Project\MATLAB\spectrogram\'; 

files = dir (strcat(path,'\*.mat'));
L = length (files);

%% 5G Signals
i = 1;
for file = files'
    signal = load(file.name);
    
    % Grab information from file
    clear waveform;
    waveform = signal.waveStruct.waveform;

    % Plots the signal
    figure("Visible",false)
    spectrogram(waveform);

    % Removes axis and colorbar
    set(gca, 'Visible', 'off');
    colorbar('off');
 
    % Saves the figure
    [C,matches] = strsplit(file.name,{'.mat','('});
    fname = strcat(C(1), sprintf('_signal_%d.png',i));
    filename = char(strcat(figuresdir, fname));
    exportgraphics(gcf,filename,'BackgroundColor','none')
    i = i + 1;
end

