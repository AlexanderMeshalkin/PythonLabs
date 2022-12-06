import pygame as pg
import numpy as np
from textures import *

FPS = 60
width = 1200
height = 800
FOV = 60
sen = 2
rays_number = 60
fov_rad = FOV * np.pi / 180
scale = width / fov_rad
MODE = "3D"
wall_height = 48
len0 = len(TEXTURES)
colors = ["BLACK", "WHITE", "GREEN", "RED", "RED", "WHITE", "BLUE", "GREEN"]
BEAMS = []

Level = [  # Square only
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 2, 2, 0, 1, 1, 0, 0, 1, 2, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 5, 0, 0, 1, 1, 1, 6, 1, 5, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 2, 2, 0, 1, 1, 0, 0, 1, 2, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1]
]

lw = len(Level)
mapscale = (height / (lw * 64))

# methods

def rotate(vec, ang):
    return np.dot(vec, [[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])


def mag(vec):
    return np.sqrt(np.sum(index ** 2 for index in vec))
