from pyglet.window import key
from pyglet.shapes import Rectangle
from pyglet.text import Label
from pyglet.graphics import Batch

from utils.utils import opposite_color, switch_opacity, read_value_from_settings, modify_setting
import config

class Button():
    def __init__(self):
        self.gravity = False

class RectangleButton(Button):
    """
    A rectangular button with a label inside.

    Parameters:
        - rectangle: a tuple (x,y,width,height) used to draw the rectangle
        - label: the string of the label
        - batch: the batch with which the rectangle and the labels should be drawn
    """

    def __init__(self, rectangle: tuple, label: str, batch : Batch = None, color: tuple = (255,255,255,125)):
        super().__init__()
        self.rectangle = Rectangle(rectangle[0], rectangle[1], rectangle[2], rectangle[3], batch=batch, color=color)
        self.label = Label(text=label, color=opposite_color(color), 
                           x=rectangle[0]+rectangle[2]//2, y=rectangle[1]+rectangle[3]//2,
                           anchor_x='center', anchor_y='center',
                           width=self.rectangle.width, align='center',
                           batch=batch, multiline=True)

    def switch_color(self, new_color: tuple = None):
        if new_color:
            self.rectangle.color = new_color
            self.label.color = opposite_color(new_color)
        else:
            #self.rectangle.color = oppositeColor(self.rectangle.color)
            #self.label.color = oppositeColor(self.label.color)
            self.rectangle.color = switch_opacity(self.rectangle.color)
            self.label.color = switch_opacity(self.label.color)

    def switch_state(self):
        self.switch_color()
    
    def press(self, symbol):
        if symbol == key.Z:
            print(self.label.text)

    def delete(self):
        self.rectangle.delete()
        self.label.delete()


class CounterButton(RectangleButton):
    """
    Button used to keep track of a value, e.g. in the settings menu
    """

    def __init__(self, rectangle: tuple, label: str, parameter: str, batch : Batch = None, color: tuple = (255,255,255,125)):
        super().__init__(rectangle, label, batch, color)
        
        self.parameter = parameter
        self.label.text = self.parameter.title() + ': ' + str(read_value_from_settings(parameter))

    def press(self, symbol):
        if symbol == key.LEFT:
            self.decrease_value()
        if symbol == key.RIGHT:
            self.increase_value()

    def decrease_value(self):
        current_setting_value = read_value_from_settings(self.parameter)
        new_value = current_setting_value - 1

        if isinstance(current_setting_value, int):
            modify_setting(self.parameter, 
                           new_value)
            
            self.label.text = self.parameter.title() + ': ' + str(new_value)

        else:
            pass

    def increase_value(self):
        current_setting_value = read_value_from_settings(self.parameter)
        new_value = current_setting_value + 1

        if isinstance(current_setting_value, int):
            modify_setting(self.parameter, 
                           new_value)
            
            self.label.text = self.parameter.title() + ': ' + str(new_value)

        else:
            pass
        

class ChangeStageButton(RectangleButton):
    """
    This button switches to a new stage, i.e. adds a new element to the stage tree.

    If save_prev_stage=False, it deletes the current element and replaces it with the target stage.
    Otherwise, it adds the target stage on top of the existing ones
    """

    def __init__(self, rectangle: tuple, label: str, batch : Batch, target_stage: str, color: tuple = (255,255,255,125), save_prev_stage: bool = False):
        super().__init__(rectangle, label, batch, color)
        self.target_stage = target_stage
        self.save_prev_stage = save_prev_stage

    def press(self, symbol):
        if symbol == key.Z:
            config.switch_stage(self.target_stage, self.save_prev_stage)


class MainMenuButton(RectangleButton):
    """
    This button resets the stages tree, deleting all data and returning to the main menu
    """

    def __init__(self, rectangle: tuple, label: str, batch : Batch, target_stage: str, color: tuple = (255,255,255,125), save_prev_stage: bool = False):
        super().__init__(rectangle, label, batch, color)
        self.target_stage = target_stage
        self.save_prev_stage = save_prev_stage

    def press(self, symbol):
        if symbol == key.Z:
            config.reset_tree()


class QuitButton(RectangleButton):
    """
    This button stops the game loop
    """

    def __init__(self, rectangle: tuple, label: str, batch : Batch, color: tuple = (255,255,255,125)):
        super().__init__(rectangle, label, batch, color)
    
    def press(self, symbol):
        if symbol == key.Z:
            config.run_game = False