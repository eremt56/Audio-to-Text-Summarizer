import tensorflow as tf
import tensorflow_datasets as tfds
import librosa as rosa


obj = tfds.load('librispeech', builder_kwargs={'config': 'lazy_decode'})
