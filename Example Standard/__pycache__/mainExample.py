import nodeCreaterExample as nc
import networkx as nx
import localsearchExample as ls
import localsearch_permutationExample as lsp
import simulatedAnnealingNewExample as sa1
import simulatedAnnealingNew2Example as sa2

# Reusable and expandeble switch-case for "Node enter" selection
def setTypeFunc(setType, sequence_):
    match setType:
        case "use example":
            sequence_ = nc.useReadySetExample(G, sequence_)
            return sequence_
        
        case "use size 5":
            sequence_ = nc.useReadySet5(G, sequence_)
            return sequence_
        
        case "use size 10":
            sequence_ = nc.useReadySet10(G, sequence_)
            return sequence_
        
        case "use size 15":
            sequence_ = nc.useReadySet15(G, sequence_)
            return sequence_
        
        case "use size 20":
            sequence_ = nc.useReadySet20(G, sequence_)
            return sequence_
        
        case "use size 30":
            sequence_ = nc.useReadySet30(G, sequence_)
            return sequence_
        
        case "add":
            sequence_ = nc.addManual(G, sequence_)
            return sequence_

#Reusable and expandeble switch-case for "type of search" selection
def searchType(processType, sequence):
    numOfIteration = int(input("Enter the number of iteration: "))
    match processType:
        case "local":
            ls.LocalSearch(G, sequence, numOfIteration)

        case "local p":
            lsp.LocalSearchPermutation(G, sequence, numOfIteration)

        case "sa1":
            sa1.SimulatedAnnealing(G, sequence, numOfIteration, 1000, 0.8, 1000)
            #SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, tempIteration, stopTemp):

        case "sa2":
            sa2.SimulatedAnnealing(G, sequence, numOfIteration, 1000, 0.8, 100, 10)
            #SimulatedAnnealing(network, initialSeq, num_Repetitions, initialTemp, coolingRate, tempIteration, stopTemp):

# Creates a graph and an empty sequence
sequenceMain = []
G = nx.Graph()

# Chooses between use ready set or add nodes manually (use/add)
setType = input("If you want to use ready set please enter the size (type: use example OR use size {5,10,15,20,30} OR add) - ")
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
                        "2: I want to use another algorithm with the same dataset\n "
                        "3: no, finish the program "))
while willContinue != 3:
    match willContinue:
        case 1:
            searchType(processType, sequenceMain)
        case 2:
            processType = input("What do you want to perform (for local search type: local,\n "
                            "for permutational local search type: local p,\n " 
                            "for simulated annealing 1 type: sa1,\n "
                            "for simulated annealing 2 type: sa2) ")
            searchType(processType, sequenceMain)

    willContinue = int(input("Do you want to perform something else?\n "   
                     "1: yes, repeat last performed algorithm\n "
                     "2: I want to use another algorithm with the same dataset\n "
                     "3: no, finish the program "))
                     