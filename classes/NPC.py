from random import shuffle
from pyglet.sprite import Sprite
from math import sqrt
from utils import load_and_resize_image
from variables import all_npcs, npc_image_paths

class NPC:
    def __init__(self, hp: int, speed: int, position: list, freedom: int, color = (125,125,125)):
        self.hp = hp
        self.speed = speed
        self.position = position
        self.initial_position = position.copy()
        self.freedom = freedom
        # Load and resize the images naming them by their file name without the path and the extension
        #chose a random image from the npc_image_paths and make it unavailable for the next npcs
        self.image = load_and_resize_image(npc_image_paths.pop())
        self.rec = Sprite(self.image, x=self.position[0], y=self.position[1])

        all_npcs.append(self)

    def update(self, dt):
            """
            Update the position of the Rectangle associated with the NPC.

            Parameters:
            dt (float): The time elapsed since the last update.
            """
            self.rec.x = self.position[0] * self.rec.width
            self.rec.y = self.position[1] * self.rec.height


    def distance_to(self, other):
        """Calculate the distance to another object."""
        return sqrt((self.position[0] - other.position[0]) ** 2 + (self.position[1] - other.position[1]) ** 2)

    def collides_with(self, other_position):
        """Check if the NPC collides with another position."""
        return self.position == other_position

    def rand_move(self, hero):
        # Stop moving if the hero is within freedom distance
        if self.distance_to(hero) <= self.freedom:
            return

        possible_moves = [(self.speed, 0), (-self.speed, 0), (0, self.speed), (0, -self.speed), (0,0), (0,0)]
        shuffle(possible_moves)

        for dx, dy in possible_moves:
            new_position = [self.position[0] + dx, self.position[1] + dy]

            # Ensure the new position is within the freedom boundary
            if (
                self.initial_position[0] - self.freedom <= new_position[0] <= self.initial_position[0] + self.freedom and
                self.initial_position[1] - self.freedom <= new_position[1] <= self.initial_position[1] + self.freedom
            ):
                # Check for collisions with the hero and other NPCs
                collision = any(npc.position == new_position for npc in all_npcs if npc != self) or new_position == hero.position
                if not collision:
                    self.position = new_position
                    break
