from app.core.utils.dominant_color_analyzer import DominantColorAnalyzer
from app.core.utils.color_analyzer_dataset import *
import app.core.utils.color_analyzer_dataset_io as dataset_io


GENERATED_FILE_NAME = "dataset.csv"
K_MEANS_CLUSTER_TOTAL = 8
FILE_PATH_FORMAT = "./Train/{}/{}.jpg"
CATEGORY_AND_FOLDER = (
    (ColorAnalyzerData.HORROR, "Horror"),
    (ColorAnalyzerData.ROMANTIC, "Romance"),
    (ColorAnalyzerData.SCIFI, "Sci-Fi")
)


def create_color_pairs(file_name):
    color_analyzer = DominantColorAnalyzer(K_MEANS_CLUSTER_TOTAL)
    color_analyzer.analyze_path(file_name)

    top_5_colors = color_analyzer.get_top_5_colors()/255.0
    top_5_colors_percentage = color_analyzer.get_top_5_colors_percentage()

    color_pairs = []
    for i in range(5):
        color_pair = ColorPairData(top_5_colors[i], top_5_colors_percentage[i])
        color_pairs.append(color_pair)

    return color_pairs


if __name__ == '__main__':
    progress = 0
    max_progress = 100 * len(CATEGORY_AND_FOLDER)
    dataset = []
    for category, folder_name in CATEGORY_AND_FOLDER:
        for index in range(100):
            file_name = FILE_PATH_FORMAT.format(folder_name, '{0:03}'.format(index+1))
            color_pairs = create_color_pairs(file_name)
            color_data = ColorAnalyzerData(color_pairs, category)
            dataset.append(color_data)

            progress += 1
            print("Progress : {:.2f}%".format(progress/max_progress * 100))

    dataset_io.save_dataset(GENERATED_FILE_NAME, dataset)
