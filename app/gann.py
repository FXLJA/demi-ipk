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
        layer_weights = []

        start_snip_index = 0
        for a, b in GANN._window_iterate_layer_shape(layer_shape):
            weight_total = (a + 1) * b
            end_snip_index = start_snip_index + weight_total
            dna_snip = numpy.array(dna[start_snip_index:end_snip_index])

            weight_matrix = dna_snip.reshape([(a + 1), b])
            layer_weights += [weight_matrix]

            start_snip_index += weight_total

        return layer_weights
