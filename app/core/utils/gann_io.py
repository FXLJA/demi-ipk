import csv
import numpy

from app.core.gann.gann import GANN
from app.config.global_config import *


def load_gann(file_name):
    training_score = 0
    test_score = 0
    gann = GANN(DEFAULT_GANN_SHAPE)

    with open(file_name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if file_name.endswith('.gnn'):
                training_score = float(row[0])
                test_score = float(row[1])
                gann.set_dna(numpy.float64(row[2:]))
            else:
                gann.set_dna(numpy.float64(row))

    return gann, training_score, test_score


def save_gann(file_name, gann, training_score, test_score):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow([training_score, test_score] + gann.get_dna())


