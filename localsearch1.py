from itertools import permutations
from simulation1 import simulate_local_search




def localSearch(G ,initial_sequence):
    # Set other parameters
    # these variables also may asked from the user
    num_repetitions = 1000
    # will be added when the time has come :P
    # Rc = 10
    # R = 100

    # Generate all possible neighborhoods by permuting the initial sequence
    neighborhoods = [list(p) for p in permutations(initial_sequence)]

    best_expected_time = float('inf')
    best_sequence = None

    # Perform local search
    for neighborhood in neighborhoods:
        # Simulate the local search algorithm for the sequence in this neighborhood
        expected_time = simulate_local_search(G, neighborhood, num_repetitions)

        # Update the best sequence and expected time if a better option is found
        if expected_time < best_expected_time:
            best_expected_time = expected_time
            best_sequence = neighborhood

    # Print the best sequence and expected time spent to check the entire network
    print("Best sequence:", best_sequence)
    print("Best expected time:", best_expected_time)