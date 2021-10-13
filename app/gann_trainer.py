from app.gann import GANN
import numpy
import random


class GANNTrainer:
    def __init__(self, population_size=100, mutation_rate=0.1, gann_shape=[20, 16, 8, 8, 3]):
        self.population_size = population_size
        self.population = numpy.array([])
        self.population_score = numpy.array([])
        self.mutation_rate = mutation_rate
        self.gann_shape = gann_shape

        self.initialization()

    def initialization(self):
        population = []
        for _i in range(self.population_size):
            population += [GANN(self.gann_shape)]
        self.population = numpy.array(population)

    def next_generation(self):
        self.evaluation()
        self.selection()
        self.reproduction()

    def evaluation(self):
        pass

    def selection(self):
        pass

    def reproduction(self):
        pass