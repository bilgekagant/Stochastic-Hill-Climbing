import nodeCreater as nc
import networkx as nx
import localsearch as ls

#reusable and expandeble switch-case for "Node enter" selection
def setTypeFunc(setType, sequence_):
    match setType:
        case "use":

            sequence_ = nc.useReadySet(G, sequence_)
            return sequence_
        case "add":
            sequence_ = nc.addManual(G, sequence_)
            return sequence_

#reusable and expandeble switch-case for "type of search" selection
def searchType(processType, sequence):
    match processType:
        case "local":
            ls.LocalSearch(G, sequence, 100)


# Creates a graph and an empty sequence
sequenceMain = []
G = nx.Graph()


# Chooses between use ready set or add nodes manually (use/add)
setType = input("Do you want to use ready set or add nodes manually (use/add) ")
sequenceMain = setTypeFunc(setType, sequenceMain)

# Chooses type of search
processType = input("What do you want to perform (for local search type: local ")
searchType(processType, sequenceMain)

# Asks if the user want to continue
willContinue = int(input("Do you want to perform something else?\n"  
                     "1: yes, repeat last local search process\n " 
                     "2: Yes, I want to add additional nodes to existing network\n "  
                     "3: no, finish the program"))
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