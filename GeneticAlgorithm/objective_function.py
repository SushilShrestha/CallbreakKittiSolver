from BruteForce.points import calculate_point

def objective_function(cards):
    '''
    Given 13 cards, group them in 4 sets of 3 cards. Calculate score for all 4 sets of cards and sum them to get final score of the card
    :param cards:
    :return: score
    '''
    score = 0
    for boundary_pointer in range(0, len(cards) - 3, 3):
        score += calculate_point(sorted(cards[boundary_pointer: boundary_pointer + 3]))
    return score


def get_points_hand(three_card_sequence):
    return calculate_point(sorted(three_card_sequence))