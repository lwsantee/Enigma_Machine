class Reflector:

    def __init__(self, wiring, name):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.name = name

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal