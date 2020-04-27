import random


def swap_mutation(phenome, mutation_rate=0.2):
    # if not (0 <= random.random() <= mutation_rate):
    #     # within mutation rate
    #     return phenome
    num_cards = len(phenome) - 1
    for card_index in range(len(phenome)):
        random_card = random.randint(0, num_cards)
        if 0 <= random.random() <= mutation_rate:
            phenome[card_index], phenome[random_card] = phenome[random_card], phenome[card_index]
    return phenome


if __name__ == '__main__':
    print(swap_mutation([1,2,3,4,5,6,7], 0.2))
