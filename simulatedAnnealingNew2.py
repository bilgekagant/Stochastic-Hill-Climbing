import math
from calculate_Expectedtime import calculate_Expectedtime
import numpy as np
import random


def SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, tempIteration, stopTemp):
    currentSeq = initialSeq.copy()
    currentCost = calculate_Expectedtime(network, currentSeq, num_Repetitions)
    
    bestSeq = currentSeq.copy()
    bestCost = currentCost

    temperature = initialTemp

    evaluationFunction = lambda seq: calculate_Expectedtime(network, seq, num_Repetitions)

    while temperature > stopTemp: #stop condition - temperature < StopCondition
        # it is going swap "tempIteration" time for each temprature
        i = 0
        while i < tempIteration:
            #swap fonksiyonu degiscek. AnnealingSwapSequence - iki random sayi belirledim sequencin 
            # uzunluguna bagli olarak sonra o sayilardaki indexi degistirdim. bir kere swap etmis oldum.
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
        temperature *= coolingRate # changes temprature by multiplying itself with cooling rate



    print("Best sequence: ", bestSeq)
    print("Best Expected Cost: ", bestCost)
    return bestSeq, bestCost

def AnnealingSwap(G, currentSeq, numRep):
    i = random.randrange(1, len(currentSeq)-1)
    j = random.randrange(1, len(currentSeq)-1)
    while i == j:
        j = random.randrange(1, len(currentSeq)-1)
    swappedSeq = currentSeq.copy()
    swappedSeq[i], swappedSeq[j] = swappedSeq[j], swappedSeq[i]

    swappedCost = calculate_Expectedtime(G, swappedSeq, numRep)

    return swappedSeq, swappedCost

