class ColorAnalyzerDataset:
    def __init__(self, dataset, training_to_test_ratio):
        self.dataset = dataset
        self.training_dataset = []
        self.test_dataset = []

        self._create_training_and_test_dataset(training_to_test_ratio)

    def _create_training_and_test_dataset(self, training_to_test_ratio):
        pass


class ColorAnalyzerData:
    def __init__(self, color_pairs, expected_result):
        self.color_pairs = color_pairs
        self.expected_result = expected_result

    def get_input(self):
        input = []
        for color_pair in self.color_pairs:
            input += color_pair.to_arr()
        return input

    def get_expected_output(self):
        return self.expected_result


class ColorPairData:
    def __init__(self, color, percentage):
        self.color = color
        self.percentage = percentage

    def to_arr(self):
        return [self.color[0], self.color[1], self.color[2], self.percentage]
