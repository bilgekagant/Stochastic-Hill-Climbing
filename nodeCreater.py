def useReadySet(graph, sequence):
    graph.add_node('X', p=1, t=0, w=0)
    graph.add_node('A', p=0.3, t=5, w=10)
    graph.add_node('B', p=0.5, t=8, w=15)
    graph.add_node('C', p=0.4, t=3, w=17)
    graph.add_node('D', p=0.2, t=4, w=23)
    graph.add_node('E', p=0.1, t=2, w=28)
    graph.add_node('Y', p=0.7, t=6, w=34)
    sequence = ['X', 'A', 'B', 'C', 'D', 'E', 'Y']
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
