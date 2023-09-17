import random

def calculate_Expectedtime(network, sequence, num_Repetitions, C):
    # Time taken for charging at each node
    CHARGING_TIME = 15

    # Total time value is adding numOfRepitations many calculated time.
    total_time = 0

    for _ in range(num_Repetitions):
        
        total_time_sequence = 0
        current_node = 'X'  # Start from node X
        current_charge = C  # Initialize the drone's charge

        for index, node in enumerate(sequence):
            properties = network.nodes[node]
            p = properties['p']
            t = properties['t']
            w = properties['w']

            # Calculate the distance between the previous node and current node.
            distancePrevious = network.nodes[current_node]['w']
            distanceNow = w
            distance = abs(distanceNow - distancePrevious)

            # Update the total time for the given sequence.
            total_time_sequence = total_time_sequence + distance + t

            # Update the current charge of the drone
            current_charge = current_charge - (distance + t)

            # Check if the current node is working by creating a random value between (0,1)
            if random.random() >= p:
                total_time += total_time_sequence
                break

            # Check if there's enough charge to move to the next node and test it
            if index + 1 < len(sequence):
                next_node = sequence[index + 1]
                next_distance = abs(network.nodes[next_node]['w'] - distanceNow)
                next_t = network.nodes[next_node]['t']

                if current_charge < (next_distance + next_t):
                    # If not enough charge, then charge the drone
                    total_time_sequence = total_time_sequence + CHARGING_TIME
                    current_charge = C  # Reset the drone's charge

            # Update node information based on given sequence.
            current_node = node
            
    # Expected time calculation.
    expected_time = total_time / num_Repetitions
    
    return expected_time

