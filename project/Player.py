from Global import *


class Player:
    def __init__(self, coord, ang, spd, omega):
        self.coord = np.array(coord)
        self.ang = ang
        self.spd = spd
        self.omega = omega

    def move(self, angle):
        self.coord = self.coord + self.spd / FPS * rotate([1, 0], angle)

    def rotate(self, dirc):
        self.ang += dirc / FPS * self.omega
        if self.ang > 2 * np.pi:
            self.ang -= 2 * np.pi
        elif self.ang < 0:
            self.ang += 2 * np.pi

    def collision(self, i, j, angle):
        shift = rotate([2 * self.spd / FPS, 0], angle)
        return [
            (self.coord[0] <= 64 * (i + 1) + 2 * self.spd / FPS) and (
                        self.coord[0] >= 64 * i - 2 * self.spd / FPS) and (
                        self.coord[1] >= 64 * j - 2 * self.spd / FPS) and (
                        self.coord[1] <= 64 * (j + 1) + 2 * self.spd / FPS),
            (self.coord[0] + shift[0] <= 64 * (i + 1) + 2 * self.spd / FPS) and (
                        self.coord[0] + shift[0] >= 64 * i - 2 * self.spd / FPS) and (
                        self.coord[1] + shift[1] >= 64 * j - 2 * self.spd / FPS) and (
                        self.coord[1] + shift[1] <= 64 * (j + 1) + 2 * self.spd / FPS)
        ]

    def increase_ang(self, value):
        self.ang += value
        if self.ang > 2 * np.pi:
            self.ang -= 2 * np.pi
        elif self.ang < 0:
            self.ang += 2 * np.pi
