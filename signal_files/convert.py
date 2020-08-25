# Converts any mp3 file into a wav file to work with python naitively
from os import path
from pydub import AudioSegment

# files                                                                         
src = "mp3\LTEsample.mp3"
dst = "wav\LTEsample.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")