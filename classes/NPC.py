from pyglet.window import key
from random import shuffle
from functions.action import action
from math import sqrt
from classes.character import Character
from variables import all_npcs

class NPC():
    def __init__(self, hp: int, speed: int, position: list, freedom: int):
        """
        Initialize the NPC with health points, speed, initial position, and movement freedom.
        
        Parameters:
        - hp (int): Health points of the NPC.
        - speed (int): Movement speed of the NPC, indicating how many units it moves per action.
        - position (list): A list containing the initial x and y coordinates of the NPC.
        - freedom (int): The maximum distance the NPC can move from its initial position. The minimum value should
                         be at least equal to the speed to allow movement. Setting freedom to a lower value than speed
                         will effectively immobilize the NPC.
        """
        self.hp = hp
        self.speed = speed
        self.position = position
        self.initial_position = position[:]  # Make a copy of the initial position
        self.freedom = freedom  # Maximum allowed distance from the initial position
    
    def distance(self, pos1, pos2):
        """
        Calculate the Euclidean distance between two points.
        """
        dx = pos1[0] - pos2[0]
        dy = pos1[1] - pos2[1]
        return sqrt(dx**2 + dy**2)

    def rand_move(self, Character: Character):
        """
        This method moves the NPC randomly within its freedom distance from the initial position.
        """
        # Check if the character is within 2 squares
        if self.distance(Character.position, self.position) <= 5:
            return

        # Define all possible directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Shuffle the directions to ensure randomness
        shuffle(directions)

        # Iterate over each direction
        for dx, dy in directions:
            # Calculate the new position
            new_position = (self.position[0] + dx, self.position[1] + dy)

            # Check if the new position is within the freedom distance from the initial position
            if (self.distance(new_position,self.initial_position) <= self.freedom):
                # If it is, update the position and return
                self.position = new_position
                return

        # If no valid move was found, the NPC stays in the same position
        return
