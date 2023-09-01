def useReadySet5(graph, sequence):
    graph.add_node('X', p=1, t=0, w=0)
    graph.add_node('1', p=0.3, t=5, w=10)
    graph.add_node('2', p=0.5, t=8, w=15)
    graph.add_node('3', p=0.4, t=3, w=17)
    graph.add_node('4', p=0.2, t=4, w=23)
    graph.add_node('5', p=0.1, t=2, w=28)
    graph.add_node('Y', p=0.7, t=6, w=34)
    sequence = ['X', '1', '2', '3', '4', '5', 'Y']
    return sequence

def useReadySet10(graph, sequence):
    graph.add_node('X', p=1, t=0, w=0)
    graph.add_node('1', p=0.3, t=5, w=10)
    graph.add_node('2', p=0.5, t=8, w=12)
    graph.add_node('3', p=0.4, t=3, w=14)
    graph.add_node('4', p=0.2, t=4, w=15)
    graph.add_node('5', p=0.1, t=2, w=16)
    graph.add_node('6', p=0.3, t=5, w=20)
    graph.add_node('7', p=0.5, t=8, w=22)
    graph.add_node('8', p=0.4, t=3, w=23)
    graph.add_node('9', p=0.2, t=4, w=25)
    graph.add_node('10', p=0.1, t=2, w=28)
    graph.add_node('Y', p=0.7, t=6, w=34)
    sequence = ['X', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Y']
    return sequence


def useReadySet15(graph, sequence):
    graph.add_node('X', p=1, t=0, w=0)
    graph.add_node('1', p=0.3, t=5, w=10)
    graph.add_node('2', p=0.5, t=8, w=15)
    graph.add_node('3', p=0.4, t=3, w=17)
    graph.add_node('4', p=0.2, t=4, w=23)
    graph.add_node('5', p=0.1, t=2, w=28)
    graph.add_node('6', p=0.3, t=5, w=30)
    graph.add_node('7', p=0.5, t=8, w=35)
    graph.add_node('8', p=0.4, t=3, w=37)
    graph.add_node('9', p=0.2, t=4, w=43)
    graph.add_node('10', p=0.1, t=2, w=45)
    graph.add_node('11', p=0.1, t=2, w=46)
    graph.add_node('12', p=0.3, t=5, w=47)
    graph.add_node('13', p=0.5, t=8, w=49)
    graph.add_node('14', p=0.4, t=3, w=50)
    graph.add_node('15', p=0.2, t=4, w=53)
    graph.add_node('Y', p=0.7, t=6, w=64)
    sequence = ['X', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', 'Y']
    return sequence

def useReadySet20(graph, sequence):
    graph.add_node('X', p=1, t=0, w=0)
    graph.add_node('1', p=0.3, t=5, w=10)
    graph.add_node('2', p=0.5, t=8, w=12)
    graph.add_node('3', p=0.4, t=3, w=17)
    graph.add_node('4', p=0.2, t=4, w=20)
    graph.add_node('5', p=0.1, t=2, w=23)
    graph.add_node('6', p=0.3, t=5, w=25)
    graph.add_node('7', p=0.5, t=8, w=27)
    graph.add_node('8', p=0.4, t=3, w=30)
    graph.add_node('9', p=0.2, t=4, w=33)
    graph.add_node('10', p=0.1, t=2, w=38)
    graph.add_node('11', p=0.1, t=2, w=39)
    graph.add_node('12', p=0.3, t=5, w=40)
    graph.add_node('13', p=0.5, t=8, w=45)
    graph.add_node('14', p=0.4, t=3, w=47)
    graph.add_node('15', p=0.2, t=4, w=53)
    graph.add_node('16', p=0.1, t=2, w=54)
    graph.add_node('17', p=0.1, t=2, w=55)
    graph.add_node('18', p=0.3, t=5, w=60)
    graph.add_node('19', p=0.5, t=8, w=63)
    graph.add_node('20', p=0.4, t=3, w=65)
    graph.add_node('Y', p=0.7, t=6, w=70)
    sequence = ['X', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'Y']
    return sequence

def useReadySet30(graph, sequence):
    graph.add_node('X', p=1, t=0, w=0)
    graph.add_node('1', p=0.3, t=5, w=10)
    graph.add_node('2', p=0.5, t=8, w=15)
    graph.add_node('3', p=0.4, t=3, w=17)
    graph.add_node('4', p=0.2, t=4, w=23)
    graph.add_node('5', p=0.1, t=2, w=28)
    graph.add_node('6', p=0.3, t=5, w=30)
    graph.add_node('7', p=0.5, t=8, w=33)
    graph.add_node('8', p=0.4, t=3, w=37)
    graph.add_node('9', p=0.2, t=4, w=40)
    graph.add_node('10', p=0.1, t=2, w=42)
    graph.add_node('11', p=0.1, t=2, w=45)
    graph.add_node('12', p=0.3, t=5, w=46)
    graph.add_node('13', p=0.5, t=8, w=48)
    graph.add_node('14', p=0.4, t=3, w=50)
    graph.add_node('15', p=0.2, t=4, w=52)
    graph.add_node('16', p=0.1, t=2, w=55)
    graph.add_node('17', p=0.1, t=2, w=60)
    graph.add_node('18', p=0.3, t=5, w=62)
    graph.add_node('19', p=0.5, t=8, w=63)
    graph.add_node('20', p=0.4, t=3, w=66)
    graph.add_node('21', p=0.3, t=5, w=67)
    graph.add_node('22', p=0.5, t=8, w=68)
    graph.add_node('23', p=0.4, t=3, w=70)
    graph.add_node('24', p=0.2, t=4, w=72)
    graph.add_node('25', p=0.1, t=2, w=73)
    graph.add_node('26', p=0.3, t=5, w=74)
    graph.add_node('27', p=0.5, t=8, w=80)
    graph.add_node('28', p=0.4, t=3, w=82)
    graph.add_node('29', p=0.2, t=4, w=86)
    graph.add_node('30', p=0.1, t=2, w=88)
    graph.add_node('Y', p=0.7, t=6, w=94)
    sequence = ['X', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', 'Y']
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
