import tensorflow as tf
import tensorflow_datasets as tfds
import librosa as rosa
import numpy as np
import os
import TrainingSample as ts

rootDirectory = "/home/eremt/Summer_Projects/Audio_to_Text_Summarizer/Small Training Set"
f = open(rootDirectory + "/6818-68772.trans.txt", "r")
line = str

sampleList = list()



lines = f.readlines()

for line in lines:
    splitLine = line.split(" ")
    sampleId = splitLine[0]
    text = line[len(sampleId) + 1:]

    audioData, samplingRate = rosa.load(rootDirectory + "/" + sampleId + ".flac")

    sample = ts.TrainingSample(audioData, samplingRate, text)

    trainingSample = sample
    sampleList.append(trainingSample)


print(sampleList[0].sampleInput)
print(sampleList[0].samplingRate)
print(sampleList[0].sampleTarget)




# data = tfds.load('librispeech', builder_kwargs={'config': 'lazy_decode'})

# text = np.array(data.size)

# audio = np.array(data.size)

# count = 0

# for pnt in data:

#     text[count] = pnt["text"]
#     audio[count] = pnt["speech"]

#     count+=1

