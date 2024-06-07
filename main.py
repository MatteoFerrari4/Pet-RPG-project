from pyglet import app, clock
from pyglet.window import Window
from classes.character import Character
from classes.NPC import NPC
from variables import height, width, all_npcs

window = Window(height=height, width=width)
fps = 30

hero = Character(30, 1, [0, 0])


Merchant1 = NPC(5, 1, [10, 10], 5)
Merchant2 = NPC(5, 1, [11, 11], 2)





def update(dt):
    hero.update(dt)
    for npc in all_npcs:
        npc.update(dt)    

@window.event
def on_key_press(symbol, arguments):
    hero.move(symbol)
    hero.update_sprite_image(symbol)
    for npc in all_npcs:
        npc.rand_move(hero)

@window.event
def on_draw():
    window.clear()
    hero.sprite.draw()
    #draw the other npcs
    for npc in all_npcs:
        npc.sprite.draw()
    


clock.schedule_interval(update, 1 / fps)
app.run()
