from os.path import dirname, join as pjoin
import scipy.io as sio

## Get the filename for a signal .mat file from the training_data dir.
##data_dir = pjoin(dirname(sio.__file__), 'training_data')
##mat_fname = pjoin(data_dir, '5G_Downlink.mat')

## Load Contents of file
mat_contents = sio.loadmat("training_data/5G_Downlink.mat")

## The result is a dictionary, one key/value pair for each variable:
sortedMat = sorted(mat_contents.keys())

waveStruct = mat_contents['waveStruct']

print(waveStruct)