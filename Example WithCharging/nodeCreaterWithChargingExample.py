def useReadySetExample(graph, sequence):
    graph.add_node('X', p=2, r=0, t=0, w=0)
    graph.add_node('1', p=0.3, r=0.1, t=5, w=12)
    graph.add_node('2', p=0.5, r=0.2, t=8, w=15)
    graph.add_node('3', p=0.4, r=0.3, t=3, w=17)
    graph.add_node('4', p=0.2, r=0.4, t=4, w=23)
    graph.add_node('Y', p=2, r=0, t=0, w=23)
    sequence = ['X', '1', '2', '3', '4', 'Y']
    return sequence
