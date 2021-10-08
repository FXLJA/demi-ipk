import numpy

from sklearn.cluster import KMeans


class DominantColorAnalyzer:
    def __init__(self, total_cluster=12):
        self.total_cluster = total_cluster
        self.image_cluster_index = None
        self.dominant_colors = None

    def analyze(self, image_data):
        km = KMeans(n_clusters=self.total_cluster)
        self.image_cluster_index = km.fit_predict(image_data)
        self.dominant_colors = km.cluster_centers_

    def get_top_5_colors(self):
        sum = numpy.bincount(self.image_cluster_index)
        return self.dominant_colors[numpy.argsort(sum)[:-6:-1]]
