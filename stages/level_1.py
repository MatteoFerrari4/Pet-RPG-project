from pyglet.graphics import Batch

from classes.blocks import Block
from classes.player import Player
from classes.stages import Level

from utils.utils import read_value_from_settings

def init_level_1():

    level_1_batch = Batch()
    level_1_objects_list = []

    floor_block = Block((0,0,read_value_from_settings('window_width'), read_value_from_settings('window_height')//6),
                        batch=level_1_batch)
    level_1_objects_list.append(floor_block)


    player = Player(x=100, y=200, hp=10, speed=1)
    level_1_objects_list.append(player)

    return Level(name='level_1', batch=level_1_batch, player=player, objects_list=level_1_objects_list)