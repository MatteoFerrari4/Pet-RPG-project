from pyglet.shapes import Rectangle
from pyglet.graphics import Batch

import numpy as np

class Block():
    
    def __init__(self, rectangle: tuple, batch: Batch, color: tuple = (255, 255, 255, 255), gravity: bool = False, mobile: bool = False, tangible: bool = True):
        self.gravity = gravity
        self.mobile = mobile
        self.tangible = tangible
        self.rectangle = Rectangle(rectangle[0], rectangle[1], rectangle[2], rectangle[3], batch=batch, color=color)

        self.velocity = np.array([0, 0])

    def update_velocity(self, acceleration: list):
        self.velocity += np.array(acceleration)
    
    def move(self, collision_direction):
        self.rectangle.x += self.velocity[0]
        self.rectangle.y += self.velocity[1]