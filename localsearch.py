from calculateCost import CalculateCost
# import pprint

def LocalSearch(G, initialSeq):
    numRepetitions = 100
    
    currentCost = CalculateCost(G, initialSeq, numRepetitions)
    print("Current Cost is: ", currentCost)

    improvedSeq, improvedCost = SwapSequence(G, initialSeq, numRepetitions)
    numberOfSwap = 0
    while currentCost > improvedCost and improvedSeq != (initialSeq or currentSeq):
        numberOfSwap += 1
        currentCost = improvedCost
        currentSeq = improvedSeq.copy()
        improvedSeq, improvedCost = SwapSequence(G, improvedSeq, numRepetitions)
        
    print("Sequences swapped: ", numberOfSwap, "times")
    print("\nBest sequence: ", improvedSeq)
    print("Best Expected Cost: ", improvedCost)

    
def SwapSequence (G, initialSeq, numRepetitions):
    seqCosts = {}

    improvedCost = float("inf")
    improvedSeq = None
    i = 1
    # For each node except start and finish
    while i <= len(initialSeq) - 3:
        j = i + 1
        # switch the node with the nodes after that except finish node
        while j <= len(initialSeq) - 2:
            switchedSeq = initialSeq.copy()
            
            switchedSeq[i], switchedSeq[j] = switchedSeq[j], switchedSeq[i]
            switchedCost = CalculateCost(G, switchedSeq, numRepetitions)
            seqCosts[tuple(switchedSeq)] = switchedCost
            
            if switchedCost < improvedCost:
                improvedCost = switchedCost
                improvedSeq = switchedSeq
            
            j += 1
        i += 1
    # print("All the sequences are: \b")
    # pprint.pprint(seqCosts)
    # print("\nBest sequence: ", improvedSeq)
    # print("Best Expected Cost: ", improvedCost)
    return improvedSeq, improvedCost
