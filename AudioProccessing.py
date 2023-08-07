import tensorflow as tf
import tensorflow_datasets as tfds
import librosa as rosa
import numpy as np
import os
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
for i in sampleList:
    if i.sampleInput > max:
        max = i.sampleInput


# Pad all audio files to be the same length
for i in range(sampleList):
    sampleList[i].sampleInput = np.pad(max)

# Data Augmentation: Time Shift? #


# Convert to audio Values to Spectrogram
spectrogramArr = np.array()

for i in range(sampleList):
    melSpectrogram = tf.raw_ops.AudioSpectrogram(sampleList[i].sampleInput)
    dB = convert to dB
    spectrogramArr.append(dB)






# data = tfds.load('librispeech', builder_kwargs={'config': 'lazy_decode'})

# text = np.array(data.size)

# audio = np.array(data.size)

# count = 0

# for pnt in data:

#     text[count] = pnt["text"]
#     audio[count] = pnt["speech"]

#     count+=1

