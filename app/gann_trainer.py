from app.gann import GANN
import numpy
import random


class GANNTrainer:
    def __init__(self, config):
        self.config = config
        self.population = numpy.array([])
        self.population_score = numpy.array([])

        if config.is_valid():
            self.initialization()
        else:
            raise Exception("Configuration not valid!")

    def initialization(self):
        population = []
        for _i in range(self.config.population_size):
            population += [GANN(self.config.gann_shape)]
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


class GANNTrainerConfig:
    def __init__(self):
        self.population_size = 100
        self.mutation_rate = 0.1
        self.gann_shape = None
        self.dataset = None

    def is_valid(self):
        return self.gann_shape is not None \
               and self.dataset is not None \
               and 0.0 < self.mutation_rate <= 1.0 \
               and 0 < self.population_size
