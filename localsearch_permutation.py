from itertools import permutations
from calculate_Expectedtime import calculate_Expectedtime


def localSearch(network, initialSeq, num_Repetitions):
    # Set other parameters
    # these variables also may asked from the user
    #num_repetitions = 1000
    # will be added when the time has come :P
    # Rc = 10
    # R = 100

    # Generate all possible neighborhoods by permuting the initial sequence
    neighborhoods = [list(p) for p in permutations(initialSeq)]

    best_expected_time = float('inf')
    best_sequence = None

    # Perform local search
    for neighborhood in neighborhoods:
        # Simulate the local search algorithm for the sequence in this neighborhood
        expected_time = calculate_Expectedtime(network, neighborhood, num_Repetitions)

        # Update the best sequence and expected time if a better option is found
        if expected_time < best_expected_time:
            best_expected_time = expected_time
            best_sequence = neighborhood

    # Print the best sequence and expected time spent to check the entire network
    print("Best sequence:", best_sequence)
    print("Best expected time:", best_expected_time)