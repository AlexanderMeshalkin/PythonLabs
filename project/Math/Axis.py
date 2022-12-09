from project.Global import *


class Axis:
    def __init__(self, pos, vector):
        self.pos = np.array(pos)
        self.vector = vector
        self.vector = self.vector.multiplyByNumber(1 / self.vector.length)
