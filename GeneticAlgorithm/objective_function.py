from BruteForce.points import calculate_point

def objective_function(cards, weights=[1,1,1,1]):
    '''
    Given 13 cards, group them in 4 sets of 3 cards. Calculate score for all 4 sets of cards and sum them to get final score of the card
    :param cards:
    :return: score
    '''
    hand_points = []
    for boundary_pointer in range(0, len(cards) - 3, 3):
        hand_points.append(get_points_hand(cards[boundary_pointer: boundary_pointer + 3]))
    hand_points = sorted(hand_points, reverse=True)

    score = 0
    for i in range(len(hand_points)):
        score += weights[i] * hand_points[i]
    return score


def get_points_hand(three_card_sequence):
    return calculate_point(sorted(three_card_sequence))