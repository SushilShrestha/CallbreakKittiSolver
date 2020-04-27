import copy

from BruteForce.cards import get_shuffled_cards, print_cards
from GeneticAlgorithm import parent_selection, recombination, survival_selection, mutation
from GeneticAlgorithm.EA_meta import EA_meta
from GeneticAlgorithm.initialize_population import generate_initial_population
from GeneticAlgorithm.objective_function import objective_function, get_points_hand

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
        parent1, parent2 = None, None
        parent1, parent2 = parent_selection_function(population)
        # parent1, parent2 = copy.deepcopy(parent1), copy.deepcopy(parent2)

        # recombine pairs of parents or mutate the resulting offspring
        child1, child2 = None, None
        child1, child2 = recombination_function(parent1, parent2)
        # child1, child2 = copy.deepcopy(child1), copy.deepcopy(child2)

        child1 = mutation_function(child1)
        child2 = mutation_function(child2)

        # evaluate new candidates
        child1_score = objective_function(child1)
        child2_score = objective_function(child2)

        # select individuals for the next generation
        population += [child1, child2]
        population_score += [child1_score, child2_score]

        population, population_score = survival_selection.replace_worst(population, population_score)
        population, population_score = list(population), list(population_score)

        ea_meta.record_iteration(population, population_score)

    return ea_meta


def get_player_points(cards_1, cards_2, cards_3, cards_4):
    points = [0, 0, 0, 0]
    for boundary_pointer in range(0, len(cards_1) - 1, 3):
        score_1 = get_points_hand(cards_1[boundary_pointer: boundary_pointer + 3])
        score_2 = get_points_hand(cards_2[boundary_pointer: boundary_pointer + 3])
        score_3 = get_points_hand(cards_3[boundary_pointer: boundary_pointer + 3])
        score_4 = get_points_hand(cards_4[boundary_pointer: boundary_pointer + 3])

        scores = [(score_1, 0), (score_2, 1), (score_3, 2), (score_4, 3)]
        scores = sorted(scores, key=lambda x: x[0], reverse=True)
        if scores[0][0] == scores[1][0]:
            # both players have same hand
            continue
        points[scores[0][1]] += 1
    return points


def simulate_game():
    cards = get_shuffled_cards()
    player1, player2, player3, player4 = cards[:13], cards[13:26], cards[26:39], cards[39:]

    ea_1 = ketti_solver_ea(
        player1,
        parent_selection_function=parent_selection.best_2_of_random_5,
        recombination_function=recombination.cut_and_crossfill_crossover,
        mutation_function=mutation.swap_mutation
    )
    ea_2 = ketti_solver_ea(
        player2,
        parent_selection_function=parent_selection.best_2_of_random_5,
        recombination_function=recombination.cut_and_crossfill_crossover,
        mutation_function=mutation.swap_mutation
    )
    ea_3 = ketti_solver_ea(
        player3,
        parent_selection_function=parent_selection.best_2_of_random_5,
        recombination_function=recombination.cut_and_crossfill_crossover,
        mutation_function=mutation.swap_mutation
    )
    ea_4 = ketti_solver_ea(
        player4,
        parent_selection_function=parent_selection.best_2_of_random_5,
        recombination_function=recombination.cut_and_crossfill_crossover,
        mutation_function=mutation.swap_mutation
    )

    best_solution1 = ea_1.get_best_solution()
    best_solution2 = ea_2.get_best_solution()
    best_solution3 = ea_3.get_best_solution()
    best_solution4 = ea_4.get_best_solution()

    points = get_player_points(best_solution1, best_solution2, best_solution3, best_solution4)
    # print(points)
    # print_cards(best_solution1)
    # print_cards(best_solution2)
    # print_cards(best_solution3)
    # print_cards(best_solution4)
    return points


if __name__ == '__main__':
    for i in range(100):
        points = simulate_game()
        print("iteration :: ", i)
        print(points)

    # ea.report()
    # print_cards(ea.get_best_solution())

    # s, y = ea.prob_distribution_of_scores(0)
    # import matplotlib.pyplot as plt
    # plt.plot(s, y)
    # plt.show()
    # print(ea.prob_distribution_of_scores(0))
    # print(my_cards[0], my_cards[1])
    # print(my_cards[0] > my_cards[1])
    # pop = generate_initial_population(my_cards)
    # for i in range(100):
    #     print_cards(pop[i], True)
    #     print(objective_function(pop[i]))
    # print_cards(my_cards, True)
    # print (objective_function(my_cards))

