from app.gann_trainer import GANNTrainer, GANNTrainerConfig
from builder.color_analyzer_dataset_builder import ColorAnalyzerDatasetBuilder


class GANNTrainerBuilder:
    def __init__(self):
        self.population_size = 100
        self.mutation_rate = 0.1
        self.gann_shape = [2, 1]
        self.dataset = ColorAnalyzerDatasetBuilder().build()

    def reset(self):
        self.__init__()

    def with_dataset(self, dataset):
        self.dataset = dataset
        return self

    def with_gann_shape(self, gann_shape):
        self.gann_shape = gann_shape
        return self

    def with_mutation_rate(self, mutation_rate):
        self.mutation_rate = mutation_rate
        return self

    def with_population_size(self, population_size):
        self.population_size = population_size
        return self

    def build(self):
        config = GANNTrainerConfig()
        config.population_size = self.population_size
        config.gann_shape = self.gann_shape
        config.mutation_rate = self.mutation_rate

        obj = GANNTrainer(self.dataset, config)
        self.reset()
        return obj
