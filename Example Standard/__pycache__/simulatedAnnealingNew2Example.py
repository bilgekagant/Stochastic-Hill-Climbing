import math, random, time
from calculate_ExpectedtimeExample import calculate_Expectedtime
import numpy as np



def SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, tempIteration, stopTemp):
    startTime = time.time()
    currentSeq = initialSeq.copy()
    currentCost = calculate_Expectedtime(network, currentSeq, num_Repetitions)
    
    bestSeq = currentSeq.copy()
    bestCost = currentCost

    temperature = initialTemp

    evaluationFunction = lambda seq: calculate_Expectedtime(network, seq, num_Repetitions)

    while temperature > stopTemp: # Stop condition - temperature < StopCondition

        # It is going to swap "tempIteration" time for each temprature
        i = 0
        while i < tempIteration:

            swappedSeq, swappedCost = AnnealingSwap(network, currentSeq, num_Repetitions)
            if evaluationFunction(swappedSeq) < evaluationFunction(currentSeq):
                currentCost = swappedCost
                currentSeq = swappedSeq.copy()
                if swappedCost < bestCost:
                    bestSeq = swappedSeq.copy()
                    bestCost = swappedCost
            else:
                deltaCost = evaluationFunction(swappedSeq) - evaluationFunction(currentSeq)
                if math.exp(-deltaCost / temperature) > np.random.rand():
                    currentCost = swappedCost
                    currentSeq = swappedSeq.copy()
            i += 1

        print("temperature", temperature)
        print("current", currentSeq, currentCost)  
        print("best", bestCost)  
        temperature *= coolingRate # Changes temprature by multiplying itself with cooling rate

    print("Best sequence: ", bestSeq)
    print("Best Expected Cost: ", bestCost)
    endTime = time.time()
    print(f"Local Search function is executed in {(endTime - startTime)*10**3:.03f}ms")
    return bestSeq, bestCost

# Swap algorithm for this simulated annealing which takes randomly two index and swap them
def AnnealingSwap(G, currentSeq, numRep):
    i = random.randrange(1, len(currentSeq)-1)
    j = random.randrange(1, len(currentSeq)-1)
    while i == j:
        j = random.randrange(1, len(currentSeq)-1)
    swappedSeq = currentSeq.copy()
    swappedSeq[i], swappedSeq[j] = swappedSeq[j], swappedSeq[i]

    swappedCost = calculate_Expectedtime(G, swappedSeq, numRep)

    return swappedSeq, swappedCost