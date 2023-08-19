import random

def CalculateCost(network, sequence, num_repetitions):
    total_cost = 0

    for _ in range(num_repetitions):
        total_cost_sequence = 0
        current_node = 'X'  # Start from node X
        previousNode = "X"

        for node in sequence:
            properties = network.nodes[node]
            p = properties['p']
            t = properties['t']
            w = properties['w']
            total_cost_sequence += w - network.nodes[previousNode]['w'] + t
            # Check if the current node is working
            if random.random() >= p:
                total_cost += total_cost_sequence
                break
            # else:
                # total_cost_sequence += w - network.nodes[previousNode]['w'] + t
            previousNode = current_node
            current_node = node


        # Check if all nodes in the sequence were visited successfully
        if current_node == sequence[-1]:
            total_cost += total_cost_sequence

    expected_time = total_cost / num_repetitions
    
    # Print the expected time spent to check the entire network
    # print("Expected time:", expected_time)
    return expected_time