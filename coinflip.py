import numpy as np

class Coin:
    def __init__(self, flipTimes):
        self.flipTimes = flipTimes 
        self.results = []
    
    def updateResults(self, randNumber):
        if randNumber <= 0.5:
            self.results.append(0) 
        else: self.results.append(1)

    def flip(self):
        if self.flipTimes == 0: return 
        for i in range(self.flipTimes):
            self.updateResults(np.random.rand(1))

    def getTotalHeads(self):
        return sum(self.results) 


if __name__ == "__main__":
    coinNum = 1000
    flipTime = 10
    experimentTimes = 100000
    coins = []
    headCounts = []
    firstCoinHeads = 0
    minCoinHeads = 0
    randCoinHeads = 0
    for i in range(experimentTimes):
        for j in range(coinNum):
            coin = Coin(flipTime) 
            coins.append(coin)
            headCounts.append(coin.getTotalHeads())

        firstCoinHeads += headCounts[0]/float(flipTime*experimentTimes)
        randCoinHeads += headCounts[np.random.randint(coinNum)]/float(flipTime*experimentTimes)
        minCoinHeads += min(headCounts)/float(flipTime*experimentTimes) 

    print "first coin heads"
    print firstCoinHeads

    print "random coin heads"
    print randCoinHeads

    print "min coin heads"
    print minCoinHeads
