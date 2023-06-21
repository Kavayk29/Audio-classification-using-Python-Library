import matplotlib.pyplot as plt
import IPython.display as ipd
import librosa 
import librosa.display

filename = '/home/kavay/Desktop/py2/audio/fold3/6988-5-0-1.wav'

plt.figure(figsize=(12,5))
data, sample_rate = librosa.load(filename)
librosa.display.AdaptiveWaveplot(data,sr=sample_rate)
ipd.Audio(filename)     