import pygame as pg
import numpy as np
from textures import *
from ray_module import *
from weapons import *
from Global import *
from Player import *
from Beam import *


class Enemy:
    def __init__(self, pos, size):
        self.pos = np.array(pos)
        self.size = size
