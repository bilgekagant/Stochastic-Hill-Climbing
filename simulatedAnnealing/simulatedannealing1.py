import random
import networkx as nx
from itertools import permutations
import math
from calculate_Expectedtime import CalculateCost

def calculate_cost(network, sequence, num_repetitions, Rc, R):
    return CalculateCost(network, sequence, num_repetitions, Rc, R)

def simulated_annealing(network, initial_sequence, num_repetitions, Rc, R, initial_temperature, cooling_rate, num_iterations):
    current_sequence = initial_sequence
    current_cost = calculate_cost(network, current_sequence, num_repetitions, Rc, R)

    best_sequence = current_sequence
    best_cost = current_cost

    for iteration in range(num_iterations):
        temperature = initial_temperature / (1 + iteration * cooling_rate)

        new_sequence = list(current_sequence)
        i, j = sorted(random.sample(range(len(new_sequence)), 2))  # Randomly select two indices to switch
        new_sequence[i], new_sequence[j] = new_sequence[j], new_sequence[i]  # Perform the switch

        new_cost = calculate_cost(network, new_sequence, num_repetitions, Rc, R)

        # If the new solution is better, accept it
        if new_cost < current_cost:
            current_sequence = new_sequence
            current_cost = new_cost

            # Update the best solution if needed
            if new_cost < best_cost:
                best_sequence = new_sequence
                best_cost = new_cost
        else:
            # If the new solution is worse, accept it with a certain probability
            probability = math.exp((current_cost - new_cost) / temperature)
            if random.random() < probability:
                current_sequence = new_sequence
                current_cost = new_cost

    return best_sequence, best_cost

# Define the network using NetworkX
G = nx.Graph()
G.add_node('X')
G.add_node('A', p=0.3, t=5, w=10)
G.add_node('B', p=0.5, t=8, w=15)
G.add_node('C', p=0.2, t=6, w=12)

# Define the initial sequence
initial_sequence = ['A', 'B', 'C']

# Set other parameters
num_repetitions = 1000
Rc = 10
R = 100
initial_temperature = 1000.0
cooling_rate = 0.03
num_iterations = 1000

# Perform Simulated Annealing
best_sequence, best_expected_time = simulated_annealing(G, initial_sequence, num_repetitions, Rc, R, initial_temperature, cooling_rate, num_iterations)

# Print the best sequence and expected time spent to check the entire network
print("Best sequence:", best_sequence)
print("Best expected time:", best_expected_time)