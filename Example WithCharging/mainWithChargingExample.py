import nodeCreaterWithChargingExample as nc
import networkx as nx
import localsearchWithChargingExample as ls
import localsearch_permutationWithChargingExample as lsp
import simulatedAnnealingNewWithChargingExample as sa1
import simulatedAnnealingNew2WithChargingExample as sa2

# Reusable and expandeble switch-case for "Node enter" selection
def setTypeFunc(setType, sequence_):
    match setType:
        case "use example":
            sequence_ = nc.useReadySetExample(G, sequence_)
            return sequence_

#Reusable and expandeble switch-case for "type of search" selection
def searchType(processType, sequence):
    numOfIteration = int(input("Enter the number of iteration: "))
    C = int(input("Enter the charge capacity of the Drone: "))
    match processType:
        case "local":
            ls.LocalSearch(G, sequence, numOfIteration, C)

        case "local p":
            lsp.LocalSearchPermutation(G, sequence, numOfIteration, C)

        case "sa1":
            sa1.SimulatedAnnealing(G, sequence, numOfIteration, 100, 0.8, 100, C)
            #SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, maxIteration, Capacity):

        case "sa2":
            sa2.SimulatedAnnealing(G, sequence, numOfIteration, 1000, 0.8, 100, 10, C)
            #SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, tempIteration, stopTemp, Capacity):

# Creates a graph and an empty sequence
sequenceMain = []
G = nx.Graph()

# Chooses between use ready set or add nodes manually (use/add)
setType = input("If you want to use ready set please enter the size (type: use example) - ")
sequenceMain = setTypeFunc(setType, sequenceMain)

# Chooses type of search
processType = input("What do you want to perform (for local search type: local,\n "
                    "for permutational local search type: local p,\n " 
                    "for simulated annealing 1 type: sa1,\n "
                    "for simulated annealing 2 type: sa2) ")
searchType(processType, sequenceMain)

# Asks if the user want to continue
willContinue = int(input("Do you want to perform something else?\n"  
                     "1: yes, repeat last performed algorithm\n "
                     "2: no, finish the program "))
while willContinue != 2:
    match willContinue:
        case 1:
            searchType(processType, sequenceMain)

    willContinue = int(input("Do you want to perform something else?\n "   
                     "1: yes, repeat last performed algorithm\n "
                     "2: no, finish the program "))