import math
import random


class ColorAnalyzerDataset:
    def __init__(self, dataset, training_to_test_ratio):
        self.dataset = dataset
        self.training_dataset = []
        self.test_dataset = []

        self._create_training_and_test_dataset(training_to_test_ratio)

    def _create_training_and_test_dataset(self, training_to_test_ratio):
        pass


class ColorAnalyzerData:
    HORROR = 0
    ROMATIC = 1
    SCIFI = 2

    def __init__(self, color_pairs, expected_result):
        self.color_pairs = color_pairs
        self.expected_result = expected_result

    def get_input(self):
        input = []
        for color_pair in self.color_pairs:
            input += color_pair.to_arr()
        return input

    def get_expected_output(self):
        if self.expected_result == ColorAnalyzerData.HORROR:
            return [1, 0, 0]
        elif self.expected_result == ColorAnalyzerData.ROMATIC:
            return [0, 1, 0]
        elif self.expected_result == ColorAnalyzerData.SCIFI:
            return [0, 0, 1]
        else:
            return [0, 0, 0]


class ColorPairData:
    def __init__(self, color, percentage):
        self.color = color
        self.percentage = percentage

    def to_arr(self):
        return [self.color[0], self.color[1], self.color[2], self.percentage]
