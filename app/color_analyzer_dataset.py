import math
import random


class ColorAnalyzerDataset:
    def __init__(self, dataset, test_ratio):
        training, test = ColorAnalyzerDataset.split_dataset(dataset, test_ratio)
        self.training_dataset = training
        self.test_dataset = test

    @staticmethod
    def split_dataset(dataset, test_ratio):
        test = []
        temp_dataset = dataset.copy()

        total_test = math.floor(len(dataset) * test_ratio)
        for _i in range(total_test):
            index = random.randrange(0, len(temp_dataset))
            test += [temp_dataset.pop(index)]

        training = temp_dataset
        return training, test


class ColorAnalyzerData:
    HORROR = 0
    ROMANTIC = 1
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
        elif self.expected_result == ColorAnalyzerData.ROMANTIC:
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
