from itertools import permutations
from calculate_ExpectedtimeWithChargingExample import calculate_Expectedtime


def LocalSearchPermutation(network, initialSeq, num_Repetitions, C):

    # Generate all possible neighborhoods by permuting the initial sequence
    nodesBetween = initialSeq[1:-1]
    neighborhoods = [list(p) for p in permutations(nodesBetween)]

    best_expected_time = float('inf')
    best_sequence = None

    # Perform local search
    for neighborhood in neighborhoods:
        # Simulate the local search algorithm for the sequence in this neighborhood
        expected_time = calculate_Expectedtime(network, neighborhood, num_Repetitions, C)

        # Update the best sequence and expected time if a better option is found
        if expected_time < best_expected_time:
            best_expected_time = expected_time
            best_sequence = neighborhood
    
    best_sequence.insert(0, 'X')
    best_sequence.append('Y')

    # Print the best sequence and expected time spent to check the entire network
    print("Best sequence:", best_sequence)
    print("Best expected time:", best_expected_time)