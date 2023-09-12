import math
from calculate_Expectedtime import calculate_Expectedtime
from localsearch import SwapSequence
import numpy as np


def SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, tempIteration, StopCondition):
    #SimulatedAnnealing(G, sequence, numOfIteration, 1000, 0.8, 10000)
    currentSeq = initialSeq.copy()
    currentCost = calculate_Expectedtime(network, currentSeq, num_Repetitions)
    bestSeq = currentSeq.copy()
    bestCost = currentCost

    temperature = initialTemp

    iteration = 0
    while iteration < maxIterations: #stop condition - temperature < StopCondition
       
       #bir temperature ile 100 kere bu islemi yap --- asagidaki 
        swappedSeq, swappedCost = SwapSequence(network, currentSeq, num_Repetitions)  #swap fonksiyonu degiscek. AnnealingSwapSequence - iki random sayi belirledim sequencin uzunluguna bagli olarak sonra o sayilardaki indexi degistirdim. bir kere swap etmis oldum.

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
        
        # yeni temperature'a gecene kadar 


        temperature *= coolingRate # temperature degisiyor burada.
        iteration += 1


    print("Best sequence: ", bestSeq)
    print("Best Expected Cost: ", bestCost)
    return bestSeq, bestCost

# ... The SwapSequence function remains unchanged ...

