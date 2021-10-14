import unittest
import numpy
from app.ann import ANN
from unittest.mock import patch


class TestANN(unittest.TestCase):
    def setUp(self):
        self.ann = ANN([2, 3, 1])

    def test_create_layer_weights(self):
        result = self.ann._create_layer_weights(2, 3)
        numpy.testing.assert_array_equal(result.shape, [3, 3])

    def test_create_all_layer_weights(self):
        self.ann.layer_weights = []
        self.ann.layer_shape = [2, 4, 3, 1]
        self.ann.init_all_layer_weights()

        numpy.testing.assert_array_equal(self.ann.layer_weights[0].shape, [3, 4])
        numpy.testing.assert_array_equal(self.ann.layer_weights[1].shape, [5, 3])
        numpy.testing.assert_array_equal(self.ann.layer_weights[2].shape, [4, 1])

    def test_constructor(self):
        numpy.testing.assert_array_equal(self.ann.layer_weights[0].shape, [3, 3])
        numpy.testing.assert_array_equal(self.ann.layer_weights[1].shape, [4, 1])

    def test_multiply_to_layer_weight(self):
        TEST_INPUT = [2, 5]
        TEST_WEIGHT = [numpy.array([[1, 2, -1], [2, 4, 0], [-1, 0, 1]])]
        EXPECTED_RESULT = numpy.array([[11, 24, -1]])

        self.ann.layer_weights = TEST_WEIGHT
        _result = self.ann._multiply_to_layer_weight(TEST_INPUT, 0)

        numpy.testing.assert_array_equal(_result, EXPECTED_RESULT)

    @patch('app.ann.activation_function.sigmoid')
    def test_forward_layer(self, mock_sigmoid):
        with patch.object(self.ann, "_multiply_to_layer_weight") as mock_multiply_weight:
            TEST_INPUT = "input data"
            EXPECTED_WEIGHT_RESULT = "weight result"
            EXPECTED_RESULT = "expected result"

            mock_multiply_weight.return_value = EXPECTED_WEIGHT_RESULT
            mock_sigmoid.return_value = EXPECTED_RESULT

            _result = self.ann._forward_layer(TEST_INPUT, 1)

            mock_multiply_weight.assert_called_with(TEST_INPUT, 1)
            mock_sigmoid.assert_called_with(EXPECTED_WEIGHT_RESULT)
            self.assertEqual(_result, EXPECTED_RESULT)

    def test_forward(self):
        TEST_INPUT = [2, 5]
        TEST_WEIGHT = [
            numpy.array([[1, 2, 2], [4, -1, 0], [-1, 0, 1]]),
            numpy.array([-1, 0, 1, 2])]
        EXPECTED_RESULT = [0.88009258]

        self.ann.layer_weights = TEST_WEIGHT

        _result = self.ann.forward(TEST_INPUT)
        numpy.testing.assert_almost_equal(_result, EXPECTED_RESULT, 0.0001)


if __name__ == '__main__':
    unittest.main()
