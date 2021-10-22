import unittest
import app.core.common.monte_carlo as monte_carlo


class TestMonteCarlo(unittest.TestCase):
    def test_generate(self):
        result = monte_carlo.generate(0.25, 10)
        self.assertEqual(10, len(result))

    def test_success(self):
        result = monte_carlo.test_success(0.0)
        self.assertFalse(result)

        result = monte_carlo.test_success(1.0)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
