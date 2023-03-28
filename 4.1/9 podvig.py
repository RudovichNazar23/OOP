class Layer:
    def __init__(self):
        self.name = "Layer"
        self.next_layer = None

    def __call__(self, obj):
        self.next_layer = obj

        return self.next_layer


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.name = "Input"
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.name = "Dense"
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        current = self.network
        while current:
            yield current
            current = current.next_layer
