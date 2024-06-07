from pyglet.shapes import Rectangle
from pyglet.window import key

import numpy as np
import math

from utils.utils import read_value_from_settings, rectangle_collision
from config import stage_tree

class Player():
    """
    The main player class
    """

    def __init__(self, x, y, hp, speed):
        self.width, self.height = 30, 30
        self.rectangle = Rectangle(x, y, self.width, self.height, color=(255, 0, 0, 255))
        self.hp = hp
        self.speed = speed

        self.velocity = np.array([0, 0]).astype('float64')

        self.mobile = True
        self.gravity = False


    def print_status(self):
        print(f'This is the player! HP: {self.hp}; Speed: {self.speed}')

    def delete(self):
        self.rectangle.delete()


    def update_velocity(self, acceleration: list):
        self.velocity += np.array(acceleration)

        self.velocity *= 0.9


    def check_collision_direction(self, block):

        rectangle_dx = Rectangle(self.rectangle.x + np.sign(self.velocity[0]), self.rectangle.y, self.width, self.height)
        rectangle_dy = Rectangle(self.rectangle.x, self.rectangle.y + np.sign(self.velocity[1]), self.width, self.height)
        collisions = [False, False]

        if rectangle_collision(rectangle_dx, block.rectangle):
            collisions[0] = True
        if rectangle_collision(rectangle_dy, block.rectangle):
            collisions[1] = True

        return collisions


    def move(self, collisions):

        if collisions[0]:
            self.velocity[0] = 0#-self.velocity[0] * 0.6
        elif collisions[1]:
            self.velocity[1] = 0#-self.velocity[1] * 0.6

        self.rectangle.x += self.velocity[0]
        self.rectangle.y += self.velocity[1]


    def read_key_press(self, pressed):
        if self.gravity:
            if pressed == key.LEFT:
                self.update_velocity([-10 * self.speed, 0])
            if pressed == key.RIGHT:
                self.update_velocity([10 * self.speed, 0])
            if pressed == key.Z:
                self.update_velocity([0, 10 * self.speed])
        
        else:
            if pressed == key.LEFT:
                self.update_velocity([-10 * self.speed, 0])
            if pressed == key.RIGHT:
                self.update_velocity([10 * self.speed, 0])
            if pressed == key.UP:
                self.update_velocity([0, 10 * self.speed])
            if pressed == key.DOWN:
                self.update_velocity([0, -10 * self.speed])


    def read_key_release(self, pressed):
        if pressed == key.LEFT:
            self.velocity[0] = 0
        if pressed == key.RIGHT:
            self.velocity[0] = 0
        if pressed == key.UP:
            self.velocity[1] = 0
        if pressed == key.DOWN:
            self.velocity[1] = 0