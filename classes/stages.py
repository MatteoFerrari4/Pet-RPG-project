from pyglet.graphics import Batch
from pyglet.window import key

from classes.player import Player
from classes.buttons import Button

class Stage():
    """
    Super-class
    One of the different stages of the game, e.g. main menu, settings, play. 
    According to the stage certain elements are displayed and the controls do different things.

    May use one for each level of the game, but idk yet
    """

    def __init__(self, name: str, batch: Batch, objects_list: list):
        self.name = name
        self.batch = batch
        self.objects_list = objects_list

class MainMenu(Stage):
    """
    Main menu of the game.
    The objects are a list of buttons.

    The controls manage button selection and button pressing.
    """

    def __init__(self, name: str, batch: Batch, objects_list: list):
        super().__init__(name, batch, objects_list)

        for obj in self.objects_list:
            obj.batch = batch
        
        self.buttons_list = [obj for obj in self.objects_list if isinstance(obj, Button)]
        self.selected_button = 0

        self.objects_list[self.selected_button].switch_state()

    def read_input(self, pressed):
        if pressed == key.UP:
            self.buttons_list[self.selected_button].switch_state()
            self.selected_button = (self.selected_button - 1) % len(self.buttons_list)
            self.buttons_list[self.selected_button].switch_state()
        if pressed == key.DOWN:
            self.buttons_list[self.selected_button].switch_state()
            self.selected_button = (self.selected_button + 1) % len(self.buttons_list)
            self.buttons_list[self.selected_button].switch_state()
        if pressed in (key.Z, key.LEFT, key.RIGHT):
            self.buttons_list[self.selected_button].press(pressed)


class Settings(Stage):
    """
    Settings menu of the game.
    The objects are a list of buttons.

    The controls manage button selection and button pressing.
    """

    def __init__(self, name: str, batch: Batch, objects_list: list):
        super().__init__(name, batch, objects_list)

        for obj in self.objects_list:
            obj.batch = batch
        
        self.buttons_list = [obj for obj in self.objects_list if isinstance(obj, Button)]
        self.selected_button = 0

        self.objects_list[self.selected_button].switch_state()

    def read_input(self, pressed):
        if pressed == key.UP:
            self.buttons_list[self.selected_button].switch_state()
            self.selected_button = (self.selected_button - 1) % len(self.buttons_list)
            self.buttons_list[self.selected_button].switch_state()
        if pressed == key.DOWN:
            self.buttons_list[self.selected_button].switch_state()
            self.selected_button = (self.selected_button + 1) % len(self.buttons_list)
            self.buttons_list[self.selected_button].switch_state()
        if pressed in (key.Z, key.LEFT, key.RIGHT):
            self.buttons_list[self.selected_button].press(pressed)


class Play(Stage):
    """
    Stage where the main gameplay takes place.
    The objects are:
        - a player
        - possibly a future GUI
    
    The class serves as a parent class for the single levels.
    The controls manage the player movements and actions which are common to all levels.
    """

    def __init__(self, name, batch, objects_list: list, player: Player):
        super().__init__(name, batch, objects_list)
        self.player = player
        self.player.rectangle.batch = batch
        
        self.objects_list.append(self.player)

    def read_input(self, pressed):
        if pressed == key.LEFT:
            self.player.rectangle.x -= 10 * self.player.speed
        if pressed == key.RIGHT:
            self.player.rectangle.x += 10 * self.player.speed
        if pressed == key.UP:
            self.player.rectangle.y += 10 * self.player.speed
        if pressed == key.DOWN:
            self.player.rectangle.y -= 10 * self.player.speed