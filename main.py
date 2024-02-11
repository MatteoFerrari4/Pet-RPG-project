from pyglet import app, clock
from pyglet.window import Window, key, mouse
from pyglet.text import Label
from pyglet.shapes import Rectangle

from classes.character import Character

window = Window(500,500)
fps = 30

hero = Character(30, 1, [0, 0])
hero_rectangle = Rectangle(hero.position[0], hero.position[1], 20, 20, color=(255,0,0))

def update(dt):
    hero_rectangle.x = hero.position[0] * hero_rectangle.width
    hero_rectangle.y = hero.position[1] * hero_rectangle.height

@window.event
def on_key_press(symbol, modifiers):
    hero.move(symbol)

@window.event
def on_draw():
    window.clear()
    hero_rectangle.draw()

clock.schedule_interval(update, 1/fps)

app.run()