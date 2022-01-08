import unittest
import app.core.common.activation_function as activation_function


class TestActivationFunction(unittest.TestCase):
    def test_sigmoid(self):
        self.assertEqual(0.5, activation_function.sigmoid(0))
        self.assertAlmostEqual(0, activation_function.sigmoid(-8), delta=0.001)
        self.assertAlmostEqual(1, activation_function.sigmoid(8), delta=0.001)


if __name__ == '__main__':
    unittest.main()
