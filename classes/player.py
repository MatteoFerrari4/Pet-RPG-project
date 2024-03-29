from pyglet.shapes import Rectangle
from pyglet.window import key

import numpy as np
from utils.utils import read_value_from_settings

class Player():
    """
    The main player class
    """

    def __init__(self, x, y, hp, speed):
        self.rectangle = Rectangle(x, y, 30, 30, color=(255, 0, 0, 255))
        self.hp = hp
        self.speed = speed

        self.velocity = np.array([0, 0])

        self.gravity = True

    def print_status(self):
        print(f'This is the player! HP: {self.hp}; Speed: {self.speed}')

    def delete(self):
        self.rectangle.delete()


    def update_velocity(self, acceleration: list):
        self.velocity += np.array(acceleration)

    def move(self):
        self.rectangle.x += self.velocity[0]
        self.rectangle.y += self.velocity[1]
        #TODO should the player check the collisions, or should the level do it?

    def read_input(self, pressed):
        if pressed == key.LEFT:
            self.rectangle.x -= 10 * self.speed
        if pressed == key.RIGHT:
            self.rectangle.x += 10 * self.speed
        if pressed == key.UP:
            self.rectangle.y += 10 * self.speed
        if pressed == key.DOWN:
            self.rectangle.y -= 10 * self.speed