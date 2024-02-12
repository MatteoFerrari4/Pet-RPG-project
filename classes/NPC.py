from pyglet.window import key
from random import randint
from functions.action import action

class NPC():
    def __init__(self, hp: int, speed: int, position: list):
        self.hp = hp
        self.speed = speed
        self.position = position
        initial_position = position


    def rand_move(self):
        if action():
            if randint(0,1)== 1:
                dir = randint(1,4)
                if dir == 1:
                    self.position[1] -= self.speed
                    dir = 0
                    #se non esce
                if dir == 2:
                    self.position[1] += self.speed
                    dir = 0
                if dir == 3:
                    self.position[0] -= self.speed
                    dir = 0
                if dir == 4:
                    self.position[0] += self.speed
                    dir = 0
                 