import numpy as np

from project.Global import *


class Vector:
    def __init__(self, pos):
        self.x = np.array(pos)[0]
        self.y = np.array(pos)[1]
        self.length = (x ** 2 + y ** 2) ** 0.5

    def add(self, vector):
        return Vector([self.x + vector.x, self.y + vector.y])

    def multiply_by_number(self, k):
        return Vector([self.x * k, self.y * k])

    def scalar_product(self, vector):
        return self.x * vector.x + self.y * vector.y

    def projection(self, axis):
        return axis.vector.multiplyByNumber(self.scalar_product(axis.vector))

    def is_collinear(self, vector):
        return self.x * vector.y == self.y * vector.x

    def is_co_directed(self, vector):
        if self.length == 0:
            return True
        if vector.length == 0:
            return True
        return self.is_collinear(vector) and (self.x * vector.x > 0 or self.y * vector.y > 0)

    def is_opposite_directed(self, vector):
        if self.length == 0:
            return True
        if vector.length == 0:
            return True
        return self.is_collinear(vector) and (self.x * vector.x < 0 or self.y * vector.y < 0)

    def convert_to_angle(self):
        if self.x == 0:
            if self.y < 0:
                return 3 * np.pi / 2
            if self.y > 0:
                return np.pi / 2
        else:
            a = np.arctan(self.y / self.x)
            if self.y >= 0 and self.x != 1:
                return a
            else:
                return np.pi + a
