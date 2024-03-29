from pyglet.graphics import Batch

from classes.buttons import ChangeStageButton, QuitButton
from classes.stages import MainMenu

from utils.utils import read_value_from_settings

ww = read_value_from_settings('window_width')
wh = read_value_from_settings('window_height')

def init_mainmenu():

    mainmenu_batch = Batch()

    mainmenu_buttons_list = []

    start_button = ChangeStageButton((ww * 0.33, 400, ww * 0.33, 75), 'Start Game', batch=mainmenu_batch, target_stage='level_1')
    mainmenu_buttons_list.append(start_button)

    settings_button = ChangeStageButton((ww * 0.33, 300, ww * 0.33, 75), 'Settings', batch=mainmenu_batch, target_stage='settings')
    mainmenu_buttons_list.append(settings_button)

    quit_button = QuitButton((ww * 0.33, 200, ww * 0.33, 75), 'Quit', batch=mainmenu_batch)
    mainmenu_buttons_list.append(quit_button)

    return MainMenu('mainmenu', batch=mainmenu_batch, objects_list=mainmenu_buttons_list)