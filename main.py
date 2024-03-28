from pyglet.window import Window, key
from pyglet import app

window = Window(800, 600)

import config

from stages.mainmenu import init_mainmenu
from stages.settings import init_settings
from stages.pausemenu import init_pausemenu
from stages.play import init_play

from classes.stages import MainMenu, Settings, Play

config.stage_tree.append(init_mainmenu())

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
        config.stage_tree[-1].read_input(symbol)

    if config.run_game == False:
        window.close()

app.run()