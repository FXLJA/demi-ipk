import numpy

class ANN:
    def __init__(self, layer_shape):
        self.layer_shape = layer_shape
        self.layer_weights = []
        self._create_all_layer_weights(layer_shape)

    def _create_all_layer_weights(self, layer_shape):
        for i in range(1, len(layer_shape)):
            new_layer_weights = self._create_layer_weights(layer_shape[i-1], layer_shape[i])
            self._append_layer_weights(new_layer_weights)

    def _append_layer_weights(self, new_layer_weights):
        self.layer_weights += [new_layer_weights]

    def _create_layer_weights(self, first_layer, second_layer):
        return numpy.random.rand(first_layer + 1, second_layer)

    def forward(self, input):
        result = input
        for i in range(len(self.layer_weights)):
            result = self._forward_layer(result, i)
        return result

    def _forward_layer(self, input, layer_index):
        z = self._multiply_to_layer_weight(input, layer_index)
        return self.sigmoid(z)

    def _multiply_to_layer_weight(self, input, layer_index):
        input_and_bias = numpy.array([numpy.append(input, 1)])
        return numpy.matmul(input_and_bias, self.layer_weights[layer_index])

    @staticmethod
    def sigmoid(x):
        return 1/(1+numpy.exp(-x))
