import math
from calculate_Expectedtime import calculate_Expectedtime
from localsearch import SwapSequence

def SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, maxIterations):
    currentSeq = initialSeq.copy()
    currentCost = calculate_Expectedtime(network, currentSeq, num_Repetitions)
    bestSeq = currentSeq.copy()
    bestCost = currentCost

    temperature = initialTemp

    iteration = 0
    while iteration < maxIterations:
        swappedSeq, swappedCost = SwapSequence(network, currentSeq, num_Repetitions)

        if swappedCost < currentCost:
            currentCost = swappedCost
            currentSeq = swappedSeq.copy()
            if swappedCost < bestCost:
                bestSeq = swappedSeq.copy()
                bestCost = swappedCost
        else:
            deltaCost = swappedCost - currentCost
            if math.exp(-deltaCost / temperature) > np.random.rand():
                currentCost = swappedCost
                currentSeq = swappedSeq.copy()
        
        temperature *= coolingRate
        iteration += 1
    
    print("Best sequence: ", bestSeq)
    print("Best Expected Cost: ", bestCost)
    return bestSeq, bestCost

# ... The SwapSequence function remains unchanged ...

# Example usage:
initialTemp = 1000
coolingRate = 0.995
maxIterations = 10000