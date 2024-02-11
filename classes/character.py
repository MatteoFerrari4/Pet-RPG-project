from pyglet.window import key

class Character():
    def __init__(self, hp: int, speed: int, position: list):
        self.hp = hp
        self.speed = speed
        self.position = position

    def move(self, pressed_key):
        if pressed_key == key.A:
            self.position[0] -= self.speed
        if pressed_key == key.D:
            self.position[0] += self.speed
        if pressed_key == key.S:
            self.position[1] -= self.speed
        if pressed_key == key.W:
            self.position[1] += self.speed

        # check_boundaries(self)