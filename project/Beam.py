from ray_module import *
from Global import *

class Beam:
    def __init__(self, lmap, coord_1, ang, length, height, thickness, qual):
        self.coord_1 = np.array(coord_1)
        self.ang = ang
        self.length = length
        self.thickness = thickness
        self.qual = qual
        self.height = height
        self.timer = 0
        # checking if the beam hits a wall
        hor_vec, ver_vec, hor_cell, ver_cell = ray(lmap, self.coord_1, self.ang)
        if min(mag(hor_vec), mag(ver_vec)) < self.length:
            self.length = min(mag(hor_vec), mag(ver_vec))
        self.coord_2 = self.coord_1 + self.length * np.array([np.cos(self.ang), np.sin(self.ang)])

    def draw(self, player, surface):
        X = np.linspace(self.coord_1[0], self.coord_2[0], self.qual)
        Y = np.linspace(self.coord_1[1], self.coord_2[1], self.qual)
        Dist = []
        Angle = []
        Visible = []

        for i in range(self.qual):
            dist = mag([X[i] - player.coord[0], Y[i] - player.coord[1]])
            Dist.append(dist)
            angle = np.arctan2((Y[i] - player.coord[1]), (X[i] - player.coord[0]))
            if angle < 0:
                angle += 2 * np.pi
            Angle.append(angle)
            # Calculating drawing props via raycast
            hor_vec, ver_vec, hor_cell, ver_cell = ray(Level, player.coord, angle)
            Visible.append(min(mag(ver_vec), mag(hor_vec)) > dist)

        for i in range(self.qual - 1):
            offset1 = Angle[i] - player.ang
            while offset1 > np.pi:
                offset1 -= 2 * np.pi
            while offset1 < - np.pi:
                offset1 += 2 * np.pi
            offset2 = Angle[i + 1] - player.ang
            while offset2 > np.pi:
                offset2 -= 2 * np.pi
            while offset2 < - np.pi:
                offset2 += 2 * np.pi
            if np.abs(offset1) < fov_rad / 2 + 1 and np.abs(offset2) < fov_rad / 2 + 1 and (
                    Visible[i] and Visible[i + 1]):
                pg.draw.line(surface, "CYAN",
                             [width / 2 + offset1 * scale, height / 2 + (self.height / Dist[i]) / np.cos(offset1)],
                             [width / 2 + offset2 * scale, height / 2 + (self.height / Dist[i + 1]) / np.cos(offset2)],
                             int(self.thickness * 2 / (Dist[i] + Dist[i + 1]) / np.cos(offset1 / 2 + offset2 / 2) / (
                                         self.timer * 10 + 1)) + 1)
                if i == 0:
                    pg.draw.circle(surface, "CYAN", [width / 2 + offset1 * scale,
                                                     height / 2 + (self.height / Dist[0]) / np.cos(offset1)],
                                   int(self.thickness / Dist[0] / 2 / np.cos(offset1) / (self.timer * 10 + 1)) + 1)
                elif i == self.qual - 2:
                    pg.draw.circle(surface, "CYAN", [width / 2 + offset2 * scale,
                                                     height / 2 + (self.height / Dist[self.qual - 1]) / np.cos(
                                                         offset2)],
                                   int(self.thickness / Dist[self.qual - 1] / 2 / np.cos(offset2) / (
                                               self.timer * 10 + 1)) + 1)
        self.timer += 1 / FPS