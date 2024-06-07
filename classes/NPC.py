from random import shuffle
from pyglet.sprite import Sprite
from math import sqrt
from utils import load_and_resize_image
from variables import all_npcs, npc_image_paths, width, height

class NPC:
    """ A class representing the non-playable characters of the game."""
    def __init__(self, hp: int, speed: int, position: list, freedom: int):
        """ Initialize the NPC with its attributes.
        hp (int): The health points of the NPC.
        speed (int): The speed of the NPC.
        position (list): The initial position of the NPC.
        freedom (int): The maximum distance the NPC can move from its initial position."""
        self.hp = hp
        self.speed = speed
        self.position = position
        self.initial_position = position.copy()
        self.freedom = freedom
        # Load and resize the images naming them by their file name without the path and the extension
        #chose a random image from the npc_image_paths and make it unavailable for the next npcs
        self.image = load_and_resize_image(npc_image_paths.pop())
        self.sprite = Sprite(self.image, x=self.position[0], y=self.position[1])

        all_npcs.append(self)

    def update(self, dt):
            """
            Update the position of the spritetangle associated with the NPC.
            Parameters:
            dt (float): The time elapsed since the last update.
            """
            self.sprite.x = self.position[0] * self.sprite.width
            self.sprite.y = self.position[1] * self.sprite.height


    def distance_to(self, other):
        """Calculate the distance to another object."""
        return sqrt((self.position[0] - other.position[0]) ** 2 + (self.position[1] - other.position[1]) ** 2)

    def collides_with(self, other_position):
        """Check if the NPC collides with another position."""
        return self.position == other_position

    def rand_move(self, hero):
        """Move the NPC randomly within their freedom's boundary and stop moving if the hero is within the freedom distance."""
        # Stop moving if the hero is within freedom distance
        if self.distance_to(hero) <= self.freedom:
            return
        # Shuffle the possible moves to make the NPC's movement random
        possible_moves = [(self.speed, 0), (-self.speed, 0), (0, self.speed), (0, -self.speed), (0,0), (0,0)]
        shuffle(possible_moves)
        # Move the NPC to a new position
        for dx, dy in possible_moves:
            new_position = [self.position[0] + dx, self.position[1] + dy]

            if (
                # Ensure the new position is within the window and within the freedom boundary
                0 <= new_position[0] * self.sprite.width < width and
                0 <= new_position[1] * self.sprite.height < height and
                self.initial_position[0] - self.freedom <= new_position[0] <= self.initial_position[0] + self.freedom and
                self.initial_position[1] - self.freedom <= new_position[1] <= self.initial_position[1] + self.freedom and
                # Ensure the new position does not collide with other NPCs
                not any(npc.position == new_position for npc in all_npcs if npc != self) or new_position == hero.position
            ):
                self.position = new_position
                break