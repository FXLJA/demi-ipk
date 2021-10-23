import csv
import numpy

from app.core.gann.gann import GANN
from app.config.global_config import *


def load_gann(file_name):
    gann = GANN(DEFAULT_GANN_SHAPE)

    with open(file_name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            gann.set_dna(numpy.float64(row))

    return gann


def save_gann(file_name, gann):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow(gann.get_dna())
