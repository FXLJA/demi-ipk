import unittest
import numpy
from builder.builders import A


class TestColorAnalyzerDataset(unittest.TestCase):
    def test_split_dataset(self):
        _dataset = A.ColorAnalyzerDataset\
            .with_total_dataset(10)\
            .with_test_ratio(0.2)\
            .build()

        self.assertEqual(len(_dataset.training_dataset), 8)
        self.assertEqual(len(_dataset.test_dataset), 2)


class TestColorAnalyzerData(unittest.TestCase):
    def test_get_input(self):
        _pair1 = A.ColorPairData\
            .with_color([1, 2, 3])\
            .with_percentage(0.5)\
            .build()
        _pair2 = A.ColorPairData\
            .with_color([-1, 0, 2])\
            .with_percentage(0.25)\
            .build()
        _analyzer_data = A.ColorAnalyzerData\
            .with_color_pairs([_pair1, _pair2])\
            .build()

        result = _analyzer_data.get_input()
        expected = [1, 2, 3, 0.5, -1, 0, 2, 0.25]

        numpy.testing.assert_array_equal(result, expected)

    def test_get_expected_output(self):
        _analyzer_data = A.ColorAnalyzerData\
            .with_expected_result_scifi()\
            .build()

        result = _analyzer_data.get_expected_output()
        expected = [0, 0, 1]

        numpy.testing.assert_array_equal(result, expected)


class TestColorPairData(unittest.TestCase):
    def test_to_arr(self):
        _color_pair = A.ColorPairData\
            .with_color([1,2,3])\
            .with_percentage(0.8)\
            .build()

        result = _color_pair.to_arr()
        expected = [1, 2, 3, 0.8]

        numpy.testing.assert_array_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
