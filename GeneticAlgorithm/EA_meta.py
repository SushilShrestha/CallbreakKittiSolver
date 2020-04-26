import copy
import numpy as np
import scipy.stats as stats


class EA_meta(object):
    population = []
    scores = []

    def record_iteration(self, population, population_score):
        self.population.append(copy.deepcopy(population))
        self.scores.append(copy.deepcopy(population_score))

    def prob_distribution_of_scores(self, iteration):
        ''''''
        scores = self.scores[0]
        scores_kde = stats.gaussian_kde(scores)
        max_score = max(*scores)
        min_score = min(*scores)
        scores = np.linspace(min_score, max_score, 1000)

        return scores, scores_kde(scores)

    def best_score_overtime(self):
        return [max(score) for score in self.scores]

    def worst_score_overtime(self):
        return [min(score) for score in self.scores]
