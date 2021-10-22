import unittest
import numpy
from unittest.mock import patch, MagicMock
from app.core.gann.gann import GANN
from app.core.utils.gann_trainer import ScoreEvaluator
from builder.builders import *


class TestGANNTrainer(unittest.TestCase):
    def test_initialization(self):
        gann_trainer = A.GANNTrainer.with_population_size(5).build()
        self.assertEqual(len(gann_trainer.population), 5)
        self.assertIsInstance(gann_trainer.population[0][0], GANN)

    @patch('app.core.utils.gann_trainer.GANNTrainer.reproduction')
    @patch('app.core.utils.gann_trainer.GANNTrainer.selection')
    @patch('app.core.utils.gann_trainer.GANNTrainer.evaluation')
    def test_next_generation(self, mock_evaluation, mock_selection, mock_reproduction):
        gann_trainer = A.GANNTrainer.build()
        gann_trainer.next_generation()

        mock_evaluation.assert_called()
        mock_selection.assert_called()
        mock_reproduction.assert_called()

    @patch('app.core.utils.gann_trainer.GANNTrainer._update_test_score')
    @patch('app.core.utils.gann_trainer.GANNTrainer._update_training_score')
    def test_evaluation(self, mock_training_score, mock_test_score):
        gann_trainer = A.GANNTrainer.build()
        gann_trainer.population = [2, 3, 4]
        gann_trainer.evaluation()

        mock_training_score.assert_called_with(4)
        mock_test_score.assert_called_with(4)

    @patch('app.core.utils.gann_trainer.ScoreEvaluator.calc_training_score')
    def test_update_training_score(self, mock_calc_score):
        mock_calc_score.return_value = 4

        mock_individual = [None, 0, 0]

        gann_trainer = A.GANNTrainer.build()
        gann_trainer._update_training_score(mock_individual)

        self.assertEqual(4, mock_individual[1])

    @patch('app.core.utils.gann_trainer.ScoreEvaluator.calc_test_score')
    def test_update_test_score(self, mock_calc_score):
        mock_calc_score.return_value = 3

        mock_individual = [None, 0, 0]

        gann_trainer = A.GANNTrainer.build()
        gann_trainer._update_test_score(mock_individual)

        self.assertEqual(3, mock_individual[2])

    @patch('app.core.utils.gann_trainer.GANNTrainer._remove_unfit_individuals')
    @patch('app.core.utils.gann_trainer.GANNTrainer.sort_population_by_training_score')
    def test_selection(self, mock_sort, mock_remove):
        gann_trainer = A.GANNTrainer.build()
        gann_trainer.selection()

        mock_sort.assert_called()
        mock_remove.assert_called()

    def test_sort_population_by_training_score(self):
        gann_trainer = A.GANNTrainer.build()
        gann_trainer.population = [(0, 7, 2), (0, 2, 4), (0, 3, 3)]
        expected = [(0, 7, 2), (0, 3, 3), (0, 2, 4)]

        gann_trainer.sort_population_by_training_score()

        numpy.testing.assert_array_equal(gann_trainer.population, expected)

    def test_remove_unfit_individuals(self):
        gann_trainer = A.GANNTrainer.with_population_size(10).build()
        gann_trainer._remove_unfit_individuals()
        self.assertEqual(len(gann_trainer.population), 5)

    def test_reproduction(self):
        gann_trainer = A.GANNTrainer.with_population_size(10).build()
        gann_trainer.population = gann_trainer.population[:5]
        gann_trainer.reproduction()
        self.assertEqual(len(gann_trainer.population), 10)

    def test_get_random_gann_in_population(self):
        gann_trainer = A.GANNTrainer.with_population_size(10).build()
        result = gann_trainer._get_random_gann_in_population()
        self.assertIn((result, 0, 0), gann_trainer.population)


class TestScoreEvaluator(unittest.TestCase):
    def test_calc_score(self):
        x = [1, 2, 3]
        y = [0, 4, 2]
        result = ScoreEvaluator._calc_score(x, y)
        expected = 1 + 2 + 1
        self.assertEqual(result, expected)

    @patch('app.core.utils.gann_trainer.ScoreEvaluator._calc_score')
    def test_calc_gann_score(self, mock_calc_score):
        mock_calc_score.return_value = -5

        mock_data = MagicMock()
        mock_data.get_input.return_value = [-2, 1, 6]
        mock_data.get_expected_output.return_value = [0, 4, 2]

        mock_gann = MagicMock()
        mock_gann.forward.return_value = [1, 2, 3]

        result = ScoreEvaluator._calc_gann_score(mock_gann, mock_data)
        expected = -5

        mock_gann.forward.assert_called_with([-2, 1, 6])
        self.assertEqual(result, expected)

    @patch('app.core.utils.gann_trainer.ScoreEvaluator._calc_gann_score')
    def test_calc_gann_dataset_score(self, mock_calc_gann_score):
        mock_calc_gann_score.return_value = 5

        mock_gann = MagicMock()
        dataset = [6, 4]

        result = ScoreEvaluator._calc_gann_dataset_score(mock_gann, dataset)
        expected = 10

        mock_calc_gann_score.assert_called_with(mock_gann, 4)
        self.assertEqual(result, expected)


class TestDatasetScoring(unittest.TestCase):
    def setUp(self):
        dataset = MagicMock()
        dataset.training_dataset = [1, 3]
        dataset.test_dataset = [2, 4]
        self.score_evaluator = ScoreEvaluator(dataset)

    @patch('app.core.utils.gann_trainer.ScoreEvaluator._calc_gann_dataset_score')
    def test_calc_training_score(self, mock_score):
        mock_score.return_value = 3

        mock_gann = MagicMock()
        result = self.score_evaluator.calc_training_score(mock_gann)

        mock_score.assert_called_with(mock_gann, [1, 3])
        self.assertEqual(3, result)

    @patch('app.core.utils.gann_trainer.ScoreEvaluator._calc_gann_dataset_score')
    def test_calc_test_score(self, mock_score):
        mock_score.return_value = -4

        mock_gann = MagicMock()
        result = self.score_evaluator.calc_test_score(mock_gann)

        mock_score.assert_called_with(mock_gann, [2, 4])
        self.assertEqual(-4, result)


if __name__ == '__main__':
    unittest.main()
