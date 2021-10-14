import unittest
import numpy
from app.gann import GANN
from unittest.mock import patch


class TestGANN(unittest.TestCase):
    def test_convert_weights_to_dna(self):
        _result = GANN.convert_weights_to_dna([[[1, 2], [3, 4]], [5, 6]])
        numpy.testing.assert_array_equal(_result, [1, 2, 3, 4, 5, 6])

    def test_convert_dna_to_weights(self):
        _shape = [1, 2, 1]
        _dna = [1, 2, 3, 4, 5, 6, 7]
        _result = GANN.convert_dna_to_weights(_dna, _shape)
        numpy.testing.assert_array_equal(_result[0], [[1, 2], [3, 4]])
        numpy.testing.assert_array_equal(_result[1], [[5], [6], [7]])


    def test_merge_dna(self):
        dna0 = [0, 2, 4, 6, 8]
        dna1 = [1, 3, 5, 7, 9]
        mask = [False, True, True, False, True]

        result = GANN.merge_dna(dna0, dna1, mask)

        numpy.testing.assert_array_equal(result, [0, 3, 5, 6, 9])

    @patch('app.gann.monte_carlo.generate')
    def test_cross_over(self, mock_monte_carlo):
        mock_monte_carlo.return_value = [True, False, True, True, False]

        gann0 = GANN([4, 1], [0, 2, 4, 6, 8])
        gann1 = GANN([4, 1], [1, 3, 5, 7, 9])
        expected = [[[1], [2], [5], [7], [8]]]

        result = gann0.cross_over(gann1)

        numpy.testing.assert_array_equal(result.layer_weights, expected)

    @patch('app.gann.random.random')
    def test_mutate_dna_with_mask(self, mock_random):
        mock_random.return_value = -3

        dna = [0, 2, 4, 6, 8]
        mask = [False, True, True, False, True]
        expected = [0, -3, -3, 6, -3]

        result = GANN.mutate_dna_with_mask(dna, mask)

        numpy.testing.assert_array_equal(result, expected)

    @patch('app.gann.random.random')
    @patch('app.gann.monte_carlo.generate')
    def test_mutate(self, mock_monte_carlo, mock_random):
        mock_monte_carlo.return_value = [False, True, True, False, True]
        mock_random.return_value = -3

        gann = GANN([4, 1], [0, 2, 4, 6, 8])
        expected = [[[0], [-3], [-3], [6], [-3]]]

        gann.mutate(0)

        numpy.testing.assert_array_equal(gann.layer_weights, expected)

    def test_mate(self):
        pass


if __name__ == '__main__':
    unittest.main()
