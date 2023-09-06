import math
from calculate_Expectedtime import calculate_Expectedtime
from localsearch import SwapSequence
import numpy as np

def SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, maxIterations):
    # Initialize inputs based on the pseudo code
    current = initialSeq.copy() # this corresponds to "current" in the pseudo code
    f = lambda seq: calculate_Expectedtime(network, seq, num_Repetitions) # this is our evaluation function
    t = lambda k: initialTemp * (coolingRate ** k) # this is our cooling schedule as a function of iteration k
    
    M = maxIterations
    k = 0
    
    bestSeq = current.copy()
    bestCost = f(bestSeq)
    
    while k < M:
        m = 0
        while m < M:
            s = SwapSequence(network, current, num_Repetitions)[0] # get the swapped sequence
            
            delta_e = f(s) - f(current)
            
            if delta_e < 0:
                current = s.copy()
                if delta_e + f(current) < bestCost:
                    bestSeq = s.copy()
                    bestCost = f(bestSeq)
            else:
                if math.exp(-delta_e / t(k)) > np.random.rand():
                    current = s.copy()
            
            m += 1
        
        k += 1

    print("Best sequence: ", bestSeq)
    print("Best Expected Cost: ", bestCost)
    return bestSeq, bestCost