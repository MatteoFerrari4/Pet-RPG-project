from pyglet.window import key
from pyglet.sprite import Sprite
from utils import load_and_resize_image
from variables import all_npcs, width, height, hero_image_paths
import os

class Character:
    """ A class representing the main character of the game."""
    def __init__(self, hp: int, speed: int, position: list):
        """ Initialize the Character with its attributes.
        hp (int): The health points of the Character.
        speed (int): The speed of the Character.
        position (list): The initial position of the Character."""
        self.hp = hp
        self.speed = speed
        self.position = position
        # Load and resize the images naming them by their file name without the path and the extension
        self.images = {os.path.basename(path).split('.')[0]: load_and_resize_image(path) for path in hero_image_paths}
        # Set the sprite to the first image
        self.sprite = Sprite(self.images['hero_right'], x=self.position[0], y=self.position[1])
        # Map keys to movement directions
        self.key_map = {
            key.A: (-self.speed, 0),  # Left
            key.D: (self.speed, 0),  # Right
            key.S: (0, -self.speed),  # Down
            key.W: (0, self.speed),  # Up
        }

    def update(self, dt):
        """
        Update the position of the Sprite associated with the Character.
        Parameters:
        dt (float): The time elapsed since the last update.
        """
        self.sprite.x = self.position[0]*self.sprite.width
        self.sprite.y = self.position[1]*self.sprite.height

    
    def collides_with(self, other_position):
        """Check if the character collides with another position."""
        return self.position == other_position
    
    def update_sprite_image(self, pressed_key):
        """
        Change the sprite image to simulate walking animation.
        these are the images that will be used for the walking animation:
        'hero_left', 'hero_right_leg_right', 'hero_right_leg_left', 
        'hero_right', 'hero_left_leg_right', 'hero_left_leg_left'.
        it will alternate hero_left_leg_left and hero_left_leg_right when moving left
        and hero_right_leg_left and hero_right_leg_right when moving right.
        when moving up it will be hero_right if he was coming from right
        and hero_left if he was coming from left.
        Parameters:
        pressed_key (int): The key that was pressed."""
        if pressed_key == key.A:  # Moving left
            if self.sprite.image == self.images['hero_left_leg_left']:
                self.sprite.image = self.images['hero_left_leg_right']
            else:
                self.sprite.image = self.images['hero_left_leg_left']
        elif pressed_key == key.D:  # Moving right
            if self.sprite.image == self.images['hero_right_leg_left']:
                self.sprite.image = self.images['hero_right_leg_right']
            else:
                self.sprite.image = self.images['hero_right_leg_left']
        # if the hero goes up or down, the sprite will be the last sprite used when moving left or right
        elif pressed_key == key.W or pressed_key == key.S:  # up
            if self.sprite.image in [self.images['hero_right_leg_right'], self.images['hero_right_leg_left'], self.images['hero_right']]:
                self.sprite.image = self.images['hero_right']
            else:
                self.sprite.image = self.images['hero_left']

    def move(self, pressed_key):
        # If the pressed key is in the key map, update the position
        if pressed_key in self.key_map:
            dx, dy = self.key_map[pressed_key]
            new_position = [self.position[0] + dx, self.position[1] + dy]
            # Ensure the new position is within the screen boundaries
            if 0 <= new_position[0]*self.sprite.width < width and 0 <= new_position[1]*self.sprite.height < height:
                # Check for collisions with NPCs
                if any(npc.position == new_position for npc in all_npcs):
                    return # Do not move if there is a collision
                else:
                    self.position = new_position