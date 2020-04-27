import random
import string

from GeneticAlgorithm.config import INITIAL_POPULATION


def replace_worst(population, population_score):
    sorted_population = sorted(zip(population, population_score), key=lambda x: x[1], reverse= True)
    top_population = sorted_population[:INITIAL_POPULATION]
    return zip(*top_population)


if __name__ == '__main__':
    def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    pop = [randomword(10) for i in range(INITIAL_POPULATION)]
    sco = [random.randint(0, 100) for i in range(INITIAL_POPULATION)]

    pop.append("hello")
    sco.append(1101)

    popu, score = replace_worst(pop, sco)
    print('hello' in popu)


