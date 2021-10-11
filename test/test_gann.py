import unittest
import numpy
from app.gann import GANN

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

    def test_cross_over_dna_at(self):
        _dna0 = [1, 2, 3, 4, 5, 6]
        _dna1 = [-1, -2, -3, -4, -5, -6]
        _start = 2
        _end = 5
        EXPECTED_DNA = [1, 2, -3, -4, -5, 6]

        _result = GANN._cross_over_dna_at(_dna0, _dna1, _start, _end)
        numpy.testing.assert_array_equal(_result, EXPECTED_DNA)


if __name__ == '__main__':
    unittest.main()
