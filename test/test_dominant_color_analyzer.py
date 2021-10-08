import unittest
import numpy
from unittest.mock import patch
from app.dominant_color_analyzer import DominantColorAnalyzer


class TestDominantColorAnalyzer(unittest.TestCase):
    def setUp(self):
        self._color_analyzer = DominantColorAnalyzer()

    @patch('app.dominant_color_analyzer.KMeans')
    def test_analyze(self, mock_color_analyzer):
        TEST_IMAGE_DATA = [[5, 6, 7]]
        EXPECTED_CLUSTER_INDEX = [3, 1, 0, 2]
        EXPECTED_DOMINANT_COLORS = [[0,1,2], [1,2,3]]

        instance = mock_color_analyzer.return_value
        instance.fit_predict.return_value = EXPECTED_CLUSTER_INDEX
        instance.cluster_centers_ = EXPECTED_DOMINANT_COLORS

        self._color_analyzer.analyze(TEST_IMAGE_DATA)

        self.assertEqual(EXPECTED_CLUSTER_INDEX, self._color_analyzer.image_cluster_index)
        self.assertEqual(EXPECTED_DOMINANT_COLORS, self._color_analyzer.dominant_colors)


    def test_get_top_5_colors(self):
        self._color_analyzer.dominant_colors = numpy.array(
            [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6]])
        self._color_analyzer.image_cluster_index = numpy.array(
            [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5])

        _result = self._color_analyzer.get_top_5_colors()

        numpy.testing.assert_array_equal(
            [[0,2], [0,3], [0,1], [0,5], [0,4]],
            _result)