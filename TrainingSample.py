

class TrainingSample:
    
    sampleInput = float()
    sampleTarget = float()
    sampleigRate = float()

    def __init__(self, sampleInput, samplingRate, sampleTarget):
        self.sampleInput = sampleInput
        self.sampleTarget = sampleTarget
        self.samplingRate = samplingRate