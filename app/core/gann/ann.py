import numpy
import app.core.common.activation_function as activation_function


class ANN:
    def __init__(self, layer_shape):
        self.layer_shape = layer_shape
        self.layer_weights = []
        self.init_all_layer_weights()

    def init_all_layer_weights(self):
        self.layer_weights = []
        for i, k in ANN._window_iterate_layer_shape(self.layer_shape):
            new_layer_weights = self._create_layer_weights(i, k)
            self.layer_weights += [new_layer_weights]

    def _create_layer_weights(self, total_start_neuron, total_end_neuron):
        return numpy.random.rand(total_start_neuron + 1, total_end_neuron) * 2 - 1

    def forward(self, input):
        result = input
        layer_total = len(self.layer_shape)

        for i in range(layer_total-1):
            result = self._forward_layer(result, i)

        return result

    def _forward_layer(self, input, layer_index):
        z = self._multiply_to_layer_weight(input, layer_index)
        return activation_function.sigmoid(z)

    def _multiply_to_layer_weight(self, input, layer_index):
        input_and_bias = numpy.array([numpy.append(input, 1)])
        return numpy.matmul(input_and_bias, self.layer_weights[layer_index])

    @staticmethod
    def _window_iterate_layer_shape(layer_shape):
        window = []
        for i in range(1, len(layer_shape)):
            window += [(layer_shape[i - 1], layer_shape[i])]
        return window
