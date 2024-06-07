from pyglet.window import Window, key
from pyglet import app, clock

import config
from utils.utils import read_value_from_settings, rectangle_collision

window = Window(read_value_from_settings('window_width'),
                read_value_from_settings('window_height'))

from stages.mainmenu import init_mainmenu
from classes.stages import Settings, Play


config.stage_tree.append(init_mainmenu())

fps = read_value_from_settings('fps')


def update(dt):
    config.stage_tree[-1].update()


@window.event
def on_draw():
    window.clear()
    config.stage_tree[-1].batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    global stage_tree

    if symbol == key.SPACE:
        if isinstance(config.stage_tree[-1], Play):
            config.switch_stage('pausemenu', save_previous_stage=True)
        elif isinstance(config.stage_tree[-1], Settings):
            config.restore_last_stage()
        else: pass

    else:
        config.stage_tree[-1].read_key_press(symbol)

    if config.run_game == False:
        window.close()


@window.event
def on_key_release(symbol, modifiers):
    if isinstance(config.stage_tree[-1], Play):
        config.stage_tree[-1].read_key_release(symbol)


clock.schedule_interval(update, 1/fps)

app.run()