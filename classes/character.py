from pyglet.window import key
from variables import all_npcs,width,height


class Character():
    def __init__(self, hp: int, speed: int, position: list):
        self.hp = hp
        self.speed = speed
        self.position = position

        # Map keys to movement directions
        self.key_map = {
            key.A: (-self.speed, 0),  # Left
            key.D: (self.speed, 0),  # Right
            key.S: (0, -self.speed),  # Down
            key.W: (0, self.speed),  # Up
        }
    
    def collides_with(self, other):
        """
        Check if the character collides with another object.

        Parameters:
        other (object): The other object to check for collision.

        Returns:
        bool: True if the character collides with the other object, False otherwise.
        """
        return self.position == other.position

    def move(self, pressed_key):
        # Store the old position
        old_position = self.position.copy()

        # If the pressed key is in the key map, update the position
        if pressed_key in self.key_map:
            dx, dy = self.key_map[pressed_key]
            self.position[0] += dx
            self.position[1] += dy

        # Check if the new position is outside the screen boundaries
        if (self.position[0] < 0 or self.position[0] > width or
            self.position[1] < 0 or self.position[1] > height):
            # If it is, reset the position to the old position
            self.position = old_position
            return

        # After moving, check for collisions with all NPCs
        for npc in all_npcs:
            if self.collides_with(npc):
            # If a collision is detected, reset the position to the old position
                self.position = old_position
                break