import random

def cut_and_crossfill_crossover(parent1, parent2):
    '''
    1. Select a random position, the crossover point, i ∈ {1, .. . , 11}
    2. Cut both parents into two segments at this position
    3. Copy the first segment of parent 1 into child 1 and the first segment of parent 2 into child 2
    4. Scan parent 2 from left to right and fill the second segment of child1 with values from parent 2, skipping those that it already contains
    5. Do the same for parent 1 and child 2

    :param parent1: list of 13 cards
    :param parent2: list of 13 cards
    :return: (child1, child2)
    '''
    i = random.randint(1, 11)
    parent_1_cut_1 = parent1[:i]
    parent_2_cut_1 = parent2[:i]

    child1 = [] + parent_1_cut_1
    child2 = [] + parent_2_cut_1

    for card in parent2:
        if card not in child1:
            child1.append(card)

    for card in parent1:
        if card not in child2:
            child2.append(card)

    return child1, child2

