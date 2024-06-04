from pyglet import app, clock
from pyglet.window import Window, key, mouse
from pyglet.text import Label
from pyglet.shapes import Rectangle
import variables
from classes.character import Character
from classes.NPC import NPC
from variables import height,width, all_npcs



window = Window(height, width)
fps = 30

hero = Character(30, 1, [0, 0])
hero_rectangle = Rectangle(hero.position[0], hero.position[1], 20, 20, color=(255,0,0))

Merchant = NPC(5, 1, [10, 10], 5)
all_npcs = [Merchant]
Merchant_tile = Rectangle(Merchant.position[0], Merchant.position[1], 20, 20, color=(0,255,0))

def update(dt):
    hero_rectangle.x = hero.position[0] * hero_rectangle.width
    hero_rectangle.y = hero.position[1] * hero_rectangle.height
    Merchant_tile.x = Merchant.position[0] * Merchant_tile.width
    Merchant_tile.y = Merchant.position[1] * Merchant_tile.height

@window.event
def on_key_press(symbol, modifiers):
    hero.move(symbol)
    Merchant.rand_move(hero)

@window.event
def on_draw():
    window.clear()
    hero_rectangle.draw()
    Merchant_tile.draw()

clock.schedule_interval(update, 1/fps)

app.run()