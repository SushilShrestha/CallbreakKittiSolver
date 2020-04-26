import copy
import random

from BruteForce.cards import get_shuffled_cards, print_cards
from GeneticAlgorithm.initialize_population import generate_initial_population
from GeneticAlgorithm.parent_selection import best_2_of_random_5
from GeneticAlgorithm.recombination import cut_and_crossfill_crossover


def test_recombination(mycards):
    parent1 = copy.deepcopy(my_cards)
    random.shuffle(parent1)
    parent2 = copy.deepcopy(my_cards)
    random.shuffle(parent2)
    child1, child2 = cut_and_crossfill_crossover(parent1, parent2)
    assert len(set(child1)) == len(set(child2))

    print_cards(parent1)
    print_cards(parent2)
    print_cards(child1)
    print_cards(child2)

def test_parent_selection(mycards):
    population = generate_initial_population(my_cards)
    a, b = best_2_of_random_5(population)
    print_cards(a)
    print_cards(b)

if __name__ == '__main__':
    cards = get_shuffled_cards()
    my_cards = cards[:13]
    print_cards(sorted(my_cards))
    print(my_cards[0], my_cards[1])
    print(my_cards[0] > my_cards[1])
    # test_recombination(my_cards)
    test_parent_selection(my_cards)
