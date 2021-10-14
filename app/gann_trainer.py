from app.gann import GANN
import random


class GANNTrainer:
    def __init__(self, config):
        self.config = config
        self.population = []
        self.population_score = []

        if config.is_valid():
            self.initialization()
        else:
            raise Exception("Configuration not valid!")

    def initialization(self):
        self.population = []
        for _i in range(self.config.population_size):
            self.population += [GANN(self.config.gann_shape)]


    def next_generation(self):
        self.evaluation()
        self.selection()
        self.reproduction()

    def evaluation(self):
        pass

    def selection(self):
        pass

    def reproduction(self):
        while len(self.population) < self.config.population_size:
            gann1 = self._get_random_gann_in_population()
            gann2 = self._get_random_gann_in_population()
            while gann1 == gann2:
                gann2 = self._get_random_gann_in_population()

            new_gann = gann1.mate(gann2)
            self.population += [new_gann]

    def _get_random_gann_in_population(self):
        index = random.randrange(0, len(self.population))
        return self.population[index]


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
               and self.population_size > 3
