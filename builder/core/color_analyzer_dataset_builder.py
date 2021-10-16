from app.core.utils.color_analyzer_dataset import *


class ColorAnalyzerDatasetBuilder:
    def __init__(self):
        self.dataset = []
        self.test_ratio = 0.0

    def reset(self):
        self.__init__()

    def with_total_dataset(self, total):
        for _i in range(total):
            self.dataset += [ColorAnalyzerDataBuilder().build()]
        return self

    def with_dataset(self, dataset):
        self.dataset = dataset
        return self

    def with_test_ratio(self, test_ratio):
        self.test_ratio = test_ratio
        return self

    def build(self):
        obj = ColorAnalyzerDataset(self.dataset, self.test_ratio)
        self.reset()
        return obj


class ColorAnalyzerDataBuilder:
    def __init__(self):
        self.color_pairs = []
        self.expected_result = 0

    def reset(self):
        self.__init__()

    def with_color_pairs(self, color_pairs):
        self.color_pairs = color_pairs
        return self

    def with_expected_result(self, expected_result):
        self.expected_result = expected_result
        return self

    def with_expected_result_horror(self):
        self.expected_result = ColorAnalyzerData.HORROR
        return self

    def with_expected_result_romantic(self):
        self.expected_result = ColorAnalyzerData.HORROR
        return self

    def with_expected_result_scifi(self):
        self.expected_result = ColorAnalyzerData.SCIFI
        return self

    def build(self):
        obj = ColorAnalyzerData(self.color_pairs, self.expected_result)
        self.reset()
        return obj


class ColorPairDataBuilder:
    def __init__(self):
        self.color = [0, 0, 0]
        self.percentage = 0.0

    def reset(self):
        self.__init__()

    def with_color(self, color) -> 'ColorPairDataBuilder':
        self.color = color
        return self

    def with_percentage(self, percentage) -> 'ColorPairDataBuilder':
        self.percentage = percentage
        return self

    def build(self) -> ColorPairData:
        obj = ColorPairData(self.color, self.percentage)
        self.reset()
        return obj
