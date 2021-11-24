import random
import app.core.common.monte_carlo as monte_carlo

from app.core.gann.gann import GANN


class GANNTrainer:
    def __init__(self, dataset, config):
        self.population = []
        self.evaluation_progress = 0
        self.best_test_score = 0
        self.score_evaluator = ScoreEvaluator(dataset)
        self.config = config

        if config.is_valid():
            self.initialization()
        else:
            raise Exception("Configuration not valid!")

    def initialization(self):
        self.population = []
        for _i in range(self.config.population_size):
            new_gann = GANN(self.config.gann_shape)
            self.add_population(new_gann)

    def add_population(self, new_gann):
        # 0: GANN, 1: Training, 2: Test
        self.population += [[new_gann, 0.0, 0.0]]

    def next_generation(self):
        self.evaluation()
        self.selection()
        self.reproduction()

    def evaluation(self):
        self.evaluation_progress = 0
        for individual in self.population:
            if individual[1] == 0.0:
                self._update_training_score(individual)
                self._update_test_score(individual)
            self.evaluation_progress += 1

    def _update_training_score(self, individual):
        gann = individual[0]
        individual[1] = self.score_evaluator.calc_training_score(gann)

    def _update_test_score(self, individual):
        gann = individual[0]

        test_score = self.score_evaluator.calc_test_score(gann)
        if test_score > self.best_test_score:
            self.best_test_score = test_score

        individual[2] = test_score

    def selection(self):
        self.sort_population_by_training_score()
        self._remove_unfit_individuals()

    def sort_population_by_training_score(self):
        self.population = sorted(self.population, key=lambda x: x[1], reverse=True)

    def _remove_unfit_individuals(self):
        # TODO : Refactor for more readability
        population_size = len(self.population)
        half_population_total = population_size * 0.5
        index = population_size
        while population_size > half_population_total:
            index = (index - 1) % population_size
            if monte_carlo.test_success(index / population_size):
                self.population.pop(index)
            population_size = len(self.population)

    def reproduction(self):
        while len(self.population) < self.config.population_size:
            gann1 = self._get_random_gann_in_population()
            gann2 = self._get_random_gann_in_population(black_list=[gann1])

            new_gann = gann1.mate(gann2, self.config.mutation_rate)
            self.add_population(new_gann)

    def _get_random_gann_in_population(self, black_list=[]):
        while True:
            index = random.randrange(0, len(self.population))
            gann = self.population[index][0]
            if gann not in black_list:
                return gann

    def set_best_gann(self, gann):
        self.population[0][0] = gann

    def get_best_gann(self):
        return self.population[0][0]

    def get_best_gann_train_score(self):
        return self.population[0][1]

    def get_best_gann_test_score(self):
        return self.population[0][2]

    def get_evaluation_progress_percentage(self):
        return self.evaluation_progress / len(self.population)


class ScoreEvaluator:
    def __init__(self, dataset):
        self.training_dataset = dataset.training_dataset
        self.test_dataset = dataset.test_dataset

    def calc_training_score(self, gann):
        return self._calc_gann_dataset_score(gann, self.training_dataset)

    def calc_test_score(self, gann):
        return self._calc_gann_dataset_score(gann, self.test_dataset)

    @staticmethod
    def _calc_gann_dataset_score(gann, dataset):
        score = 0.0
        for data in dataset:
            score += ScoreEvaluator._calc_gann_score(gann, data)
        return score / len(dataset)

    @staticmethod
    def _calc_gann_score(gann, data):
        input = data.get_input()
        output = gann.forward(input)[0]
        expected_output = data.get_expected_output()
        return ScoreEvaluator._calc_score(output, expected_output)

    @staticmethod
    def _calc_score(x, y):
        score = 0.0
        for i in range(len(x)):
            if y[i] == 1:
                score += abs(x[i] - y[i]) * 2
            else:
                score += abs(x[i] - y[i])
        score = 1.0 - (score * 0.25)

        return score


class GANNTrainerConfig:
    def __init__(self):
        self.population_size = 100
        self.mutation_rate = 0.1
        self.gann_shape = None

    def is_valid(self):
        return self.gann_shape is not None \
               and 0.0 < self.mutation_rate <= 1.0 \
               and self.population_size > 3
