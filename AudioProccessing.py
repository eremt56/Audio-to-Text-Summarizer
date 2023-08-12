import tensorflow as tf
import tensorflow_io as tfio
import tensorflow_datasets as tfds
import librosa as rosa
import numpy as np
import os
import matplotlib
from matplotlib import pyplot as plt
import TrainingSample as ts

# Extract data from .txt file, put in list of TrainingSample
rootDirectory = "/home/eremt/Summer_Projects/Audio_to_Text_Summarizer/Small Training Set"
f = open(rootDirectory + "/6818-68772.trans.txt", "r")
line = str

sampleList = list()

lines = f.readlines()

# Insert data into data object "TrainingSample"
for line in lines:
    splitLine = line.split(" ")
    sampleId = splitLine[0]
    text = line[len(sampleId) + 1:]

    audioData, samplingRate = rosa.load(rootDirectory + "/" + sampleId + ".flac")

    sample = ts.TrainingSample(audioData, samplingRate, text)

    trainingSample = sample
    sampleList.append(trainingSample)


# Find maximum audio file length
max = 0
for i in range(len(sampleList)):
    if len(sampleList[i].sampleInput) > max:
        max = len(sampleList[i].sampleInput)


# Pad all audio files to be the same length
for i in range(len(sampleList)):
    amountToPad = max - len(sampleList[i].sampleInput)
    sampleList[i].sampleInput = np.pad(sampleList[i].sampleInput, (0, amountToPad), 'constant', constant_values=(0, 0))
    print(sampleList[i].sampleInput)
    # sampleList[i].sampleInput = np.pad(sampleList[i].sampleInput, ((0, 0), (0, amountToPad)), 'constant', constant_values=(0))
    

# Data Augmentation: Time Shift? #



# Convert to audio Values to Spectrogram
spectrogramArr = np.array(1)

for i in range(len(sampleList)):

    spectrogram = tfio.audio.spectrogram(sampleList[i].sampleInput, nfft=512, window=512, stride=256)
    mel_spectrogram = tfio.audio.melscale(spectrogram, rate=sampleList[i].samplingRate, mels=128, fmin=0, fmax=8000)

    dbscale_mel_spectrogram = tfio.audio.dbscale(mel_spectrogram, top_db=80)

    spectrogramArr = np.append(spectrogramArr, dbscale_mel_spectrogram)


plt.plot(spectrogramArr)
plt.savefig("Test.png")





# data = tfds.load('librispeech', builder_kwargs={'config': 'lazy_decode'})

# text = np.array(data.size)

# audio = np.array(data.size)

# count = 0

# for pnt in data:

#     text[count] = pnt["text"]
#     audio[count] = pnt["speech"]

#     count+=1

