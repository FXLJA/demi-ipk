import numpy
import unittest

from app.KMeans import KMeans


class TestRandomVector(unittest.TestCase):
    def setUp(self):
        self._kmeans = KMeans()

    def test_ShouldReturnNotNone_WhenCalled(self):
        _result = self._kmeans.GetRandomCentroidPosition()
        self.assertIsNotNone(_result)

    def test_ShouldReturnNumpy_WhenCalled(self):
        _result = self._kmeans.GetRandomCentroidPosition()
        self.assertIsInstance(_result, numpy.ndarray)

    def test_ShouldReturnArraySize3_WhenCalled(self):
        _result = self._kmeans.GetRandomCentroidPosition()
        self.assertEqual(3, _result.size)

    def test_ShouldReturnRandomVector0to1_WhenCalled(self):
        _result = self._kmeans.GetRandomCentroidPosition()
        self.assertAlmostEqual(0.5, _result[0], delta=0.5)
        self.assertAlmostEqual(0.5, _result[1], delta=0.5)
        self.assertAlmostEqual(0.5, _result[2], delta=0.5)

    def test_ShouldReturnDifferentVectors_WhenCalledTwice(self):
        _result1 = self._kmeans.GetRandomCentroidPosition()
        _result2 = self._kmeans.GetRandomCentroidPosition()
        self.assertTrue((_result1 != _result2).any())


if __name__ == '__main__':
    unittest.main()
