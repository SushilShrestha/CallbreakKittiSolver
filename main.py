import time
start_time = time.time()

from operator import add
from itertools import combinations
from Cards import get_shuffled_cards, print_cards
from Points import calculate_point

def get_possible_combinations(cards):
    if len(cards) < 3:
        return [[]]

    big_basket = []

    possible_card_seqs = combinations(cards, 3)

    for card_seq in possible_card_seqs:
        card_seq = sorted(card_seq, key=lambda x: x.number)
        used_cards_uuids = [x.uuid for x in card_seq]
        remaining_cards = filter(lambda x: x.uuid not in used_cards_uuids, cards)

        remaining_cards_combination = get_possible_combinations(remaining_cards)

        for card_combinations in remaining_cards_combination:
            card_combinations.append(card_seq)

        big_basket += remaining_cards_combination
    return big_basket


if __name__ == '__main__':
    cards = get_shuffled_cards()
    print 'Calculating Combinations...'
    my_cards = cards[:13]
    possible_combinations = get_possible_combinations(my_cards)

    print 'Combinations Ready!! ' + str(len(possible_combinations)) + " Possible combinations"
    print("\n--- %s seconds ---" % (time.time() - start_time))
    print 'Now Calculating Best Possible Combinations...'

    highest_point = 0
    best_combination = []
    for card_combination in possible_combinations:
        points = reduce(lambda x, y: x + calculate_point(y), card_combination, 0)
        if points > highest_point:
            highest_point = points
            best_combination = card_combination

    best_combination = sorted(best_combination, key=lambda x: calculate_point(x), reverse=True)
    print_cards(my_cards)
    print
    map(print_cards, best_combination)

    print("\n--- %s seconds ---" % (time.time() - start_time))



    # possible_first_sets = combinations(my_cards, 3)
    # for first_set in possible_first_sets:
    #     first_set_uuids = [x.uuid for x in first_set]
    #     remaining_cards = filter(lambda x: x.uuid not in first_set_uuids, my_cards)

        # possible_second_set = combinations(remaining_cards, 3)




    # trails, runs,  = []
    # map(print_cards, filter(is_trail, possible_triplets))
    # print
    # map(print_cards, filter(is_a_run, possible_triplets))
    # print
    # map(print_cards, filter(is_of_same_color, possible_triplets))
    # print
    # map(print_cards, filter(is_a_judh, possible_triplets))
