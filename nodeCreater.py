def useReadySet(graph, sequence):
    graph.add_node('X', w=0)
    graph.add_node('A', p=0.3, t=5, w=10)
    graph.add_node('B', p=0.5, t=8, w=15)
    graph.add_node('C', p=0.2, t=6, w=12)
    sequence = ['A', 'B', 'C']
    return sequence

def addManual(graph, sequence):
    c = "y"
    while c == "y":
        # if (graph.('X'))
        print("Caution: c value is the distance to start point X")
        name = input("Enter desired Node name  (node_name) ")
        properties= input("Enter desired Node properties p_value t_value w_value)").split()
        p_ = float(properties[0])
        t_ = float(properties[1])
        w_ = float(properties[2])
        graph.add_node(name, p=p_, t=t_, w=w_)
        c = input("Do you want to add another Node? (y/n)")
        sequence = sequence.append(name)
    return sequence
