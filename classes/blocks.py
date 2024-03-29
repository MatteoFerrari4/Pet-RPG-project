from pyglet.shapes import Rectangle
from pyglet.graphics import Batch

class Block():
    
    def __init__(self, rectangle: tuple, batch: Batch, color: tuple = (255, 255, 255, 255)):
        self.gravity = False
        self.tangible = True

        self.rectangle = Rectangle(rectangle[0], rectangle[1], rectangle[2], rectangle[3], batch=batch, color=color)