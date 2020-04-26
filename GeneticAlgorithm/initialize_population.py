import copy
import random
from .config import INITIAL_POPULATION


def generate_initial_population(cards):
    population = []
    for i in range(INITIAL_POPULATION):
        card_set = copy.deepcopy(cards)
        random.shuffle(card_set)
        population.append(card_set)
    return population
