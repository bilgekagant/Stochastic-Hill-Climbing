# Use calculate_Expectedtime function.
from calculate_Expectedtime import calculate_Expectedtime

def LocalSearch(network, initialSeq, num_Repetitions):

    currentSeq = initialSeq.copy()
    currentCost = calculate_Expectedtime(network, currentSeq, num_Repetitions)

    print("Current Cost is: ", currentCost)

    numberOfSwap = 1

    swappedBestSeq, swappedBestCost = SwapSequence(network, currentSeq, num_Repetitions)

    while currentCost > swappedBestCost and swappedBestSeq != (initialSeq or currentSeq): #esitlik durumu?
        print("Current Sequence", currentSeq, "Swapped Best Sequence", swappedBestSeq)
        print("Current Cost: ", currentCost, "Swapper Best Cost", swappedBestCost)
        numberOfSwap += 1
        currentCost = swappedBestCost
        currentSeq = swappedBestSeq.copy()
        swappedBestSeq, swappedBestCost = SwapSequence(network, swappedBestSeq, num_Repetitions)
        
    print("Sequences swapped: ", numberOfSwap, "times")
    print("\nBest sequence: ", currentSeq)
    print("Best Expected Cost: ", currentCost)

    
def SwapSequence (network, currentSeq, num_Repetitions):
    seqCosts = {}

    swappedBestCost = float("inf")
    swappedBestSeq = None
    i = 1
    # For each node except start and finish
    while i <= len(currentSeq) - 3:
        j = i + 1
        # switch the node with the nodes after that except finish node
        while j <= len(currentSeq) - 2:
            switchedSeq = currentSeq.copy()
            
            switchedSeq[i], switchedSeq[j] = switchedSeq[j], switchedSeq[i]
            switchedCost = calculate_Expectedtime(network, switchedSeq, num_Repetitions)
            seqCosts[tuple(switchedSeq)] = switchedCost
            
            if switchedCost < swappedBestCost:
                swappedBestCost = switchedCost
                swappedBestSeq = switchedSeq
            
            j += 1
        i += 1

    print("All the sequences are: \b")
    print(seqCosts)
    print("\nBest sequence: ", swappedBestSeq)
    print("Best Expected Cost: ", swappedBestCost)
    return swappedBestSeq, swappedBestCost
