import copy
import datetime

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

from GeneticAlgorithm.objective_function import get_points_hand


class EA_meta(object):
    def __init__(self):
        self.population = []
        self.scores = []

    def get_num_iterations(self):
        return len(self.population)

    def get_best_solution(self):
        return list(self.sort_cards_wrt_hands_score(self.population[-1][0]))

    def sort_cards_wrt_hands_score(self, cards):
        scoremap = []
        for boundary_pointer in range(0, len(cards) - 3, 3):
            score = get_points_hand(cards[boundary_pointer: boundary_pointer + 3])
            scoremap.append((boundary_pointer, score))

        scoremap = sorted(scoremap, key=lambda x: x[1], reverse=True)
        for index, score in scoremap:
            yield cards[index]
            yield cards[index + 1]
            yield cards[index + 2]



    def record_iteration(self, population, population_score):
        self.population.append(copy.deepcopy(population))
        self.scores.append(copy.deepcopy(population_score))

    def prob_distribution_of_scores(self, iteration, start=None, end=None):
        ''''''
        scores = self.scores[iteration]
        scores_kde = stats.gaussian_kde(scores)
        max_score = max(*scores) if end == None else end
        min_score = min(*scores) if start == None else start
        scores = np.linspace(min_score, max_score, 1000)

        return scores, scores_kde(scores)

    def best_score_overtime(self):
        return [max(score) for score in self.scores]

    def worst_score_overtime(self):
        return [min(score) for score in self.scores]

    def report(self):
        num_iterations = self.get_num_iterations()

        start_index, halfway_index, end_index = 0, num_iterations // 2, -1
        max_score = max(self.scores[start_index] + self.scores[halfway_index] + self.scores[end_index])
        min_score = min(self.scores[start_index] + self.scores[halfway_index] + self.scores[end_index])

        scores, initial_prob_dist = self.prob_distribution_of_scores(0, max_score, min_score)
        _, halfway_prob_dist = self.prob_distribution_of_scores(num_iterations // 2, max_score, min_score)
        _, final_prob_dist = self.prob_distribution_of_scores(num_iterations - 1, max_score, min_score)

        randkey = datetime.datetime.now().microsecond

        plt.plot(scores, initial_prob_dist)
        plt.title('Initial Probability distribution of objective function')
        plt.xlabel('Score')
        plt.ylabel('Probability')
        plt.savefig('output/initial_prob{}.png'.format(randkey))
        # plt.show()
        plt.clf()

        plt.plot(scores, halfway_prob_dist)
        plt.title('Halfway Probability distribution of objective function')
        plt.xlabel('Score')
        plt.ylabel('Probability')
        plt.savefig('output/halfway_prob{}.png'.format(randkey))
        # plt.show()
        plt.clf()

        plt.plot(scores, final_prob_dist)
        plt.title('Final Probability distribution of objective function')
        plt.xlabel('Score')
        plt.ylabel('Probability')
        plt.savefig('output/end_prob{}.png'.format(randkey))
        # plt.show()
        plt.clf()

        best_score = list(map(max, self.scores))
        worst_score = list(map(min, self.scores))
        avg_score = list(map(lambda x: sum(x)/len(x), self.scores))

        plt.plot(best_score, label='Best score')
        plt.plot(worst_score, label='Worst score')
        plt.plot(avg_score, label='Average score')
        plt.xlabel('Number of Iteration')
        plt.ylabel('Score')
        plt.legend()
        plt.savefig('output/scores{}.png'.format(randkey))
        # plt.show()
        plt.clf()

