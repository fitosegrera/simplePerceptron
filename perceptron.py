from numpy import random

gInputs = []

class Perceptron():

    def setWeights(self, weightNum):
        weights = []
        for i in range(weightNum):
            weights.append(random.rand() * 2 - 1)
        return weights

    def activate(self, weights, inputs):
        global gInputs
        gInputs = inputs
        sum = 0
        for i in range(len(inputs)):
            sum += weights[i] * inputs[i]
        if sum >= 0:
            return 1
        else:
            return -1

    def updateWeights(self, learningRate, desired, sum):
        global gInputs
        newWeights = []
        print "DESIRED ", desired
        if desired != sum:
            error = desired - sum
            print "ERROR ", error
            length = len(gInputs)
            for i in range(0, length):
                newWeights.append(learningRate * error * gInputs[i])
            return {'newWeights': newWeights, 'iterate': True}
        else:
            print "SUCCESS"
            return {'newWeights': newWeights, 'iterate': False}
