import numpy
import scipy
import matplotlib
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


class DominantColorAnalyzer:
    def GetDominantColors(self, image):
        km = KMeans(n_clusters=1)
        km.fit_predict(image)
        return km.cluster_centers_
