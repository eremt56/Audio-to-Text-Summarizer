import random

class TrainingSample:
    
    sampleInput = float()
    sampleTarget = float()
    samplingRate = float()

    def __init__(self, sampleInput, samplingRate, sampleTarget):
        self.sampleInput = sampleInput
        self.sampleTarget = sampleTarget
        self.samplingRate = samplingRate

 
    def time_shift(self, aud, shift_limit):
        sig, sr = aud
        _, sig_len = sig.shape
        shift_amt = int(random.random() * shift_limit * sig_len)
        return (sig.roll(shift_amt), sr)

    
   
