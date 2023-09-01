import nodeCreater as nc
import networkx as nx
import localsearch as ls
import localsearch_permutation as lsp

# Reusable and expandeble switch-case for "Node enter" selection
def setTypeFunc(setType, sequence_):
    match setType:
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
    match processType:
        case "local":
            ls.LocalSearch(G, sequence, 1000)

        case "local permutation":
            lsp.LocalSearchPermutation(G, sequence, 1000)

# Creates a graph and an empty sequence
sequenceMain = []
G = nx.Graph()

# Chooses between use ready set or add nodes manually (use/add)
setType = input("Do you want to use ready set or add nodes manually. If you want to use ready set please enter the size (type: use size {5,10,15,20,30} OR add) - ")
sequenceMain = setTypeFunc(setType, sequenceMain)

# Chooses type of search
processType = input("What do you want to perform (for local search type: local or for permutational local search type: local permutation) - ")
searchType(processType, sequenceMain)

# Asks if the user want to continue
willContinue = int(input("Do you want to perform something else?\n"  
                     "1: yes, repeat last local search process\n " 
                     "2: Yes, I want to add additional nodes to existing network\n "  
                     "3: no, finish the program "))
while willContinue != 3:
    match willContinue:
        case 1:
            searchType(processType, sequenceMain)
        case 2:
            setTypeFunc("add", sequenceMain)

    willContinue = int(input("Do you want to perform something else?\n "   
                     "1: yes, repeat last local search process\n "  
                     "2: Yes, I want to add additional nodes to existing network\n "   
                     "3: no, finish the program "))