import numpy as np

class Coin:
    def __init__(self):
        self.flipTimes = 0
        self.results = []
    
    def updateResults(self, randNumber):
        if randNumber <= 0.5:
            self.results.append(0) 
        else: self.results.append(1)

    def flip(self):
        self.flipTimes += 1
        self.updateResults(np.random.rand(1))

    def getResults(self):
        return self.results

    def getFlipTimes(self):
        return self.flipTimes


if __name__ == "__main__":
    coinNum = 1000
    flipTime = 10
    experimentTimes = 100000
