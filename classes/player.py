from pyglet.shapes import Rectangle, Circle
from time import perf_counter

class Player():
    """
    The main player class
    """

    def __init__(self, x, y, hp, speed):
        self.rectangle = Rectangle(x, y, 30, 30, color=(255, 0, 0, 255))
        self.hp = hp
        self.speed = speed

    def print_status(self):
        print(f'This is the player! HP: {self.hp}; Speed: {self.speed}')

    def delete(self):
        self.rectangle.delete()
