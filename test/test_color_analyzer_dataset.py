import unittest
import numpy
from builder.builders import A


class TestColorAnalyzerDataset(unittest.TestCase):
    def test_create_training_and_test_dataset(self):
        pass


class TestColorAnalyzerData(unittest.TestCase):
    def test_get_input(self):
        pass

    def test_get_expected_output(self):
        pass


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
