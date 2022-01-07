import unittest
import numpy
from unittest.mock import patch
from app.core.utils.dominant_color_analyzer import DominantColorAnalyzer


class TestDominantColorAnalyzer(unittest.TestCase):
    def setUp(self):
        self._color_analyzer = DominantColorAnalyzer(8)

    @patch('app.core.utils.dominant_color_analyzer.cv2')
    def test_analyze_path(self, mock_cv2):
        TEST_IMAGE_PATH = "image_path"
        EXPECTED_IMAGE_RESULT = "image_result"
        EXPECTED_HSV_RESULT = "hsv_result"

        mock_cv2.COLOR_BGR2HSV = -1
        mock_cv2.imread.return_value = EXPECTED_IMAGE_RESULT
        mock_cv2.cvtColor.return_value = EXPECTED_HSV_RESULT

        with patch.object(self._color_analyzer, "analyze_image") as mock_analyze_image:
            self._color_analyzer.analyze_path(TEST_IMAGE_PATH)

            mock_cv2.imread.assert_called_with(TEST_IMAGE_PATH)
            mock_analyze_image.assert_called_with(EXPECTED_HSV_RESULT)

    @patch('app.core.utils.dominant_color_analyzer.KMeans')
    def test_analyze_image(self, mock_kmeans):
        TEST_IMAGE_DATA = [[5, 6, 7]]
        EXPECTED_CLUSTER_INDEX = [3, 1, 0, 2]
        EXPECTED_DOMINANT_COLORS = [[0,1,2], [1,2,3]]

        instance = mock_kmeans.return_value
        instance.fit_predict.return_value = EXPECTED_CLUSTER_INDEX
        instance.cluster_centers_ = EXPECTED_DOMINANT_COLORS

        self._color_analyzer.analyze_image(TEST_IMAGE_DATA)

        self.assertEqual(EXPECTED_CLUSTER_INDEX, self._color_analyzer.image_cluster_index)
        self.assertEqual(EXPECTED_DOMINANT_COLORS, self._color_analyzer.dominant_colors)

    def test_get_top_5_colors(self):
        TEST_COLORS = [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6]]
        TEST_CLUSTER = [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5]
        EXPECTED_RESULT = [[0,2], [0,3], [0,1], [0,5], [0,4]]

        self._color_analyzer.dominant_colors = numpy.array(TEST_COLORS)
        self._color_analyzer.image_cluster_index = numpy.array(TEST_CLUSTER)

        _result = self._color_analyzer.get_top_5_colors()

        numpy.testing.assert_array_equal(_result, EXPECTED_RESULT)


if __name__ == '__main__':
    unittest.main()
