from pyglet.window import key
from random import randint
from functions.action import action

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

    def distance_from_initial(self, new_position):
        # Calculate the Manhattan distance from the initial position
        return abs(new_position[0] - self.initial_position[0]) + abs(new_position[1] - self.initial_position[1])

    def rand_move(self):
        if action():
            directions = [1, 2, 3, 4]  # Possible directions
            while directions:  # While there are directions left to try
                dir = randint(0, len(directions) - 1)  # Select a random index from remaining directions
                chosen_direction = directions[dir]  # Get the direction at the selected index
                new_position = self.position[:]  # Copy the current position to calculate the potential new position

                # Adjust the new_position based on the chosen direction
                if chosen_direction == 1:
                    new_position[1] -= self.speed
                elif chosen_direction == 2:
                    new_position[1] += self.speed
                elif chosen_direction == 3:
                    new_position[0] -= self.speed
                elif chosen_direction == 4:
                    new_position[0] += self.speed

                # Check if the new position is within the allowed distance from the initial position
                if self.distance_from_initial(new_position) <= self.freedom:
                    self.position = new_position  # Update the position if within bounds
                    break  # Exit the loop since a valid move was found
                else:
                    directions.remove(chosen_direction)  # Remove the invalid direction and try again

            # If no valid direction was found, the NPC does not move this turn
