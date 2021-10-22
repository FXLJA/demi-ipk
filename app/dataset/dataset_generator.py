import cv2

from app.core.utils.dominant_color_analyzer import DominantColorAnalyzer
from app.core.utils.color_analyzer_dataset import *
import app.core.utils.color_analyzer_dataset_io as dataset_io


def create_color_pairs(file_name):
    color_analyzer = DominantColorAnalyzer()
    color_analyzer.analyze_path(file_name)

    top_5_colors = color_analyzer.get_top_5_colors()
    top_5_colors_percentage = color_analyzer.get_top_5_colors_percentage()

    color_pairs = []
    for i in range(5):
        color_pair = ColorPairData(top_5_colors[i], top_5_colors_percentage[i])
        color_pairs.append(color_pair)

    return color_pairs


if __name__ == '__main__':
    file_path_format = "./posters/{}/{}.jpg"
    folder_dict = {
        ColorAnalyzerData.HORROR : "Horror",
        ColorAnalyzerData.ROMANTIC : "Romance",
        ColorAnalyzerData.SCIFI : "Sci-Fi"
    }

    dataset = []
    for expected_result, folder_name in folder_dict.items():
        for index in range(100):
            file_name = file_path_format.format(folder_name, index+1)
            color_pairs = create_color_pairs(file_name)

            color_data = ColorAnalyzerData(color_pairs, folder_name)
            dataset.append(color_data)

    dataset_io.save_dataset("test.csv", dataset)
