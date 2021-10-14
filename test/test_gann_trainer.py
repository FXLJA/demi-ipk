import unittest
from app.gann_trainer import GANNTrainer
from app.gann import GANN
from builder.builders import A


class TestGANNTrainer(unittest.TestCase):
    def test_initialization(self):
        gann_trainer = A.GANNTrainer.with_population_size(5).build()
        self.assertEqual(len(gann_trainer.population), 5)
        self.assertIsInstance(gann_trainer.population[0], GANN)


if __name__ == '__main__':
    unittest.main()
