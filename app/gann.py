from app.ann import ANN
import numpy
import random


class GANN(ANN):
    def mate(self, target, mutation_rate=0.01):
        pass

    def mutate(self, mutation_rate=0.01):
        pass

    def cross_over(self, target):
        dna_self = self.convert_weights_to_dna(self.layer_weights)
        dna_target = self.convert_weights_to_dna(target.layer_weights)
        start_point = random.randrange(len(dna_self)-1)
        end_point = random.randrange(start_point+1, len(dna_self))
        return self._cross_over_dna_at(dna_self, dna_target, start_point, end_point)

    @staticmethod
    def _cross_over_dna_at(dna0, dna1, start, end):
        return dna0[:start] + dna1[start:end] + dna0[end:]

    @staticmethod
    def convert_weights_to_dna(layer_weights):
        dna = []
        for layer_weights in layer_weights:
            for w in numpy.array(layer_weights).flat:
                dna += [w]
        return dna

    @staticmethod
    def convert_dna_to_weights(dna, layer_shape):
        i = 0
        layer_weights = []

        for a, b in GANN._window_iterate_layer_shape(layer_shape):
            total = (a + 1) * b
            layer_weights += [numpy.array(dna[i:i+total]).reshape([(a + 1), b])]
            i += total

        return layer_weights
