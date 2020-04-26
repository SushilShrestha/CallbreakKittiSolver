import copy

from BruteForce.cards import get_shuffled_cards, print_cards
from GeneticAlgorithm import parent_selection, recombination, survival_selection
from GeneticAlgorithm.EA_meta import EA_meta
from GeneticAlgorithm.initialize_population import generate_initial_population
from GeneticAlgorithm.objective_function import objective_function


NUM_GENERATIONS = 1000


def ketti_solver_ea(cards,
                    parent_selection_function,
                    recombination_function,
                    mutation_function
                    ):
    ea_meta = EA_meta()

    population = generate_initial_population(cards)
    population_score = [objective_function(pop) for pop in population]

    for i in range(NUM_GENERATIONS):
        # select parents (high score with high prob low with low prob)
        parent1, parent2 = parent_selection_function(population)

        # recombine pairs of parents or mutate the resulting offspring
        child1, child2 = recombination_function(parent1, parent2)

        # evaluate new candidates
        child1_score = objective_function(child1)
        child2_score = objective_function(child2)

        # select individuals for the next generation
        population += [child1, child2]
        population_score += [child1_score, child2_score]

        population, population_score = survival_selection.replace_worst(population, population_score)
        population, population_score = list(population), list(population_score)

        ea_meta.record_iteration(population, population_score)

    print_cards(population[0])
    print_cards(population[1])

    return ea_meta


if __name__ == '__main__':
    cards = get_shuffled_cards()
    my_cards = cards[:13]
    print_cards(sorted(my_cards))

    ea = ketti_solver_ea(
        my_cards,
        parent_selection_function=parent_selection.best_2_of_random_5,
        recombination_function=recombination.cut_and_crossfill_crossover,
        mutation_function=lambda x: None
    )
    s, y = ea.prob_distribution_of_scores(0)
    import matplotlib.pyplot as plt
    plt.plot(s, y)
    plt.show()
    print(ea.prob_distribution_of_scores(0))
    # print(my_cards[0], my_cards[1])
    # print(my_cards[0] > my_cards[1])
    # pop = generate_initial_population(my_cards)
    # for i in range(100):
    #     print_cards(pop[i], True)
    #     print(objective_function(pop[i]))
    # print_cards(my_cards, True)
    # print (objective_function(my_cards))

