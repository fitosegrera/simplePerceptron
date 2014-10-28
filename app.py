from perceptron import Perceptron

inputs = [-1,-1,1]
weightNum = len(inputs)
weights = 0
learningRate = 0.01
desired = 1
iterate = True
iterCount = 0

ptron = Perceptron()
weights = ptron.setWeights(weightNum)
while iterate:
    print "-"*70
    print "Initial Weights: ", weights
    sum = ptron.activate(weights, inputs)
    print "Sum: ", sum
    returned = ptron.updateWeights(learningRate, desired, sum)
    print "New Weights: ", returned['newWeights']
    if not returned['iterate']:
        print "Iterations: ", iterCount
        iterate = False
        print "-"*70
    else:
        weights = returned['newWeights']
        iterCount = iterCount + 1
