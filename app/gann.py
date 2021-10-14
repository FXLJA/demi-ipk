from app.ann import ANN
import numpy
import random
import app.monte_carlo as monte_carlo


# TODO : Refactor to Create DNA class
class GANN(ANN):
    def __init__(self, layer_shape, dna=None):
        if dna is None:
            super().__init__(layer_shape)
        else:
            self.layer_shape = layer_shape
            self.layer_weights = GANN.convert_dna_to_weights(dna, layer_shape)

    def mate(self, target, mutation_rate):
        new_gann = self.cross_over(target)
        new_gann.mutate(mutation_rate)
        return new_gann

    def mutate(self, mutation_rate):
        dna = self.get_dna()
        mask = monte_carlo.generate(mutation_rate, len(dna))
        new_dna = GANN.mutate_dna_with_mask(dna, mask)
        self.set_dna(new_dna)

    @staticmethod
    def mutate_dna_with_mask(dna, mask):
        new_dna = dna.copy()
        for i in range(len(mask)):
            if mask[i]:
                new_dna[i] = random.random()
        return new_dna

    def cross_over(self, target):
        dna_self = self.get_dna()
        dna_target = target.get_dna()
        mask = monte_carlo.generate(0.5, len(dna_self))
        new_dna = GANN.merge_dna(dna_self, dna_target, mask)
        return GANN(self.layer_shape, new_dna)

    def get_dna(self):
        return GANN.convert_weights_to_dna(self.layer_weights)

    def set_dna(self, new_dna):
        self.layer_weights = GANN.convert_dna_to_weights(new_dna, self.layer_shape)

    @staticmethod
    def merge_dna(dna0, dna1, mask):
        new_dna = []
        for i in range(len(mask)):
            if mask[i]:
                new_dna += [dna1[i]]
            else:
                new_dna += [dna0[i]]
        return new_dna

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

        # TODO : Refactor for more readability
        start_snip_index = 0
        for a, b in ANN._window_iterate_layer_shape(layer_shape):
            weight_total = (a + 1) * b
            end_snip_index = start_snip_index + weight_total
            dna_snip = numpy.array(dna[start_snip_index:end_snip_index])

            weight_matrix = dna_snip.reshape([(a + 1), b])
            layer_weights += [weight_matrix]

            start_snip_index += weight_total

        return layer_weights
