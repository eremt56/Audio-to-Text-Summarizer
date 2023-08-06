import tensorflow as tf
import tensorflow_datasets as tfds
import librosa as rosa
import numpy as np

data = tfds.load('librispeech', builder_kwargs={'config': 'lazy_decode'})

text = np.array(data.size)

audio = np.array(data.size)

count = 0

for pnt in data:

    text[count] = pnt["text"]
    audio[count] = pnt["speech"]

    count+=1

