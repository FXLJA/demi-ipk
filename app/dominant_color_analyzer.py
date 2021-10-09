import numpy
import cv2

from sklearn.cluster import KMeans


class DominantColorAnalyzer:
    def __init__(self, total_cluster=12):
        self.total_cluster = total_cluster
        self.image_cluster_index = None
        self.dominant_colors = None

    def analyze_path(self, image_path):
        image = cv2.imread(image_path)
        hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        self.analyze_image(hsvImage)

    def analyze_image(self, image_data):
        km = KMeans(n_clusters=self.total_cluster)
        self.image_cluster_index = km.fit_predict(image_data)
        self.dominant_colors = km.cluster_centers_

    def get_top_5_colors(self):
        sum = numpy.bincount(self.image_cluster_index)
        return self.dominant_colors[numpy.argsort(sum)[:-6:-1]]
