import csv
import numpy

from app.core.utils.color_analyzer_dataset import *


def load_dataset(file_name):
    raw_dataset = []

    with open(file_name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            raw_dataset += [row]

    dataset = []
    for raw_data in raw_dataset:
        color_pairs = []
        for i in range(5):
            color = numpy.float64([raw_data[i*4], raw_data[i*4+1], raw_data[i*4+2]])
            color_pair = ColorPairData(color, float(raw_data[i*4+3]))
            color_pairs.append(color_pair)

        color_data = ColorAnalyzerData(color_pairs, int(raw_data[4*5]))
        dataset.append(color_data)

    return dataset


def save_dataset(file_name, dataset):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for data in dataset:
            row_data = data.get_input() + [data.expected_result]
            writer.writerow(row_data)
