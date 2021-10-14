import unittest
from app.gann import GANN
from builder.builders import A


class TestGANNTrainer(unittest.TestCase):
    def test_initialization(self):
        gann_trainer = A.GANNTrainer.with_population_size(5).build()
        self.assertEqual(len(gann_trainer.population), 5)
        self.assertIsInstance(gann_trainer.population[0], GANN)

    def test_next_generation(self):
        pass

    def test_evaluation(self):
        pass

    def test_selection(self):
        gann_trainer = A.GANNTrainer.with_population_size(10).build()
        gann_trainer.selection()
        self.assertEqual(len(gann_trainer.population), 5)

    def test_reproduction(self):
        gann_trainer = A.GANNTrainer.with_population_size(10).build()
        gann_trainer.population = gann_trainer.population[:5]
        gann_trainer.reproduction()
        self.assertEqual(len(gann_trainer.population), 10)

    def test_get_random_gann_in_population(self):
        gann_trainer = A.GANNTrainer.with_population_size(10).build()
        result = gann_trainer._get_random_gann_in_population()
        self.assertIn(result, gann_trainer.population)


if __name__ == '__main__':
    unittest.main()
