import random

# Calculate the expected time spent to visit a network with given sequence. 
# Inputs: network(given as graph), sequence might change depending on the points will be visited and num of repitations to calculate expected time.

def calculate_Expectedtime(network, sequence, num_Repetitions):
    # Total time value is adding numOfRepitations many calculated time.
    total_time = 0

    for _ in range(num_Repetitions):
        
        total_time_sequence = 0
        current_node = 'X'  # Start from node X
        previousNode = "X"

        for node in sequence:
            properties = network.nodes[node]
            p = properties['p']
            t = properties['t']
            w = properties['w']
            # Update the total time for the given sequence.
            # Since w - distance from point X to current node, this calculates the distance between previous node - current node.
            total_time_sequence += w - network.nodes[previousNode]['w'] + t
            # Check if the current node is working by creating a random value between (0,1)
            if random.random() >= p:
                total_time += total_time_sequence
                break
            # Else - will continue to loop by itself.

            # Update node information based on given sequence.
            previousNode = current_node
            current_node = node
    # Expected time calculation.
    expected_time = total_time / num_Repetitions
    
    # Print the expected time spent to check the entire network
    # print("Expected time:", expected_time)
    return expected_time