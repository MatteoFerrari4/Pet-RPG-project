from pyglet.graphics import Batch

from classes.buttons import ChangeStageButton, CounterButton
from classes.stages import Settings


def init_settings():

    settings_batch = Batch()
    settings_buttons_list = []

    volume_button = CounterButton((300, 400, 200, 75), label=f'Volume', parameter='volume', batch=settings_batch)
    settings_buttons_list.append(volume_button)

    gamma_button = CounterButton((300, 300, 200, 75), label=f'Gamma', parameter='gamma', batch=settings_batch)
    settings_buttons_list.append(gamma_button)

    main_menu_button = ChangeStageButton((300, 50, 200, 75), label='Back', batch=settings_batch, target_stage='mainmenu')
    settings_buttons_list.append(main_menu_button)

    return Settings('settings', objects_list=settings_buttons_list, batch=settings_batch)