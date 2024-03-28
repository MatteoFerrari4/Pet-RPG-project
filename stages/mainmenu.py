from pyglet.graphics import Batch

from classes.buttons import ChangeStageButton, QuitButton
from classes.stages import MainMenu


def init_mainmenu():

    mainmenu_batch = Batch()

    mainmenu_buttons_list = []

    start_button = ChangeStageButton((300, 400, 200, 75), 'Start Game', batch=mainmenu_batch, target_stage='play')
    mainmenu_buttons_list.append(start_button)

    settings_button = ChangeStageButton((300, 300, 200, 75), 'Settings', batch=mainmenu_batch, target_stage='settings')
    mainmenu_buttons_list.append(settings_button)

    quit_button = QuitButton((300, 200, 200, 75), 'Quit', batch=mainmenu_batch)
    mainmenu_buttons_list.append(quit_button)

    return MainMenu('mainmenu', batch=mainmenu_batch, objects_list=mainmenu_buttons_list)