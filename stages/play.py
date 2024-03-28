from pyglet.graphics import Batch

from classes.player import Player
from classes.stages import Play


def init_play():

    play_batch = Batch()
    play_objects_list = []

    player = Player(x=100, y=100, hp=30, speed=1)
    play_objects_list.append(player)

    return Play('play', batch=play_batch, objects_list=play_objects_list, player=player)