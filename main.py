import turtle
import random
import math
from _tkinter import TclError

# Other module imports
from classdefs import Button, btns, Tile, tilesList, TileField

# Window boilerplate
wn = turtle.Screen()
wn.title('Questionable means of exploration')
wn.setup(height = 800, width = 800)
wn.bgcolor('#464646'); wn.listen(); wn.tracer(0)

# Exiting
wn.onkeypress(turtle.bye, 'Escape')

# Tiles
world = TileField(2, 'water')

# 'Scrolling' in all directions
def up():
	for tile in tilesList:
		tile.t.sety(tile.t.ycor() - 20) # It's minus because only the screen is 'going up'

def down():
	for tile in tilesList:
		tile.t.sety(tile.t.ycor() + 20)

def left():
	for tile in tilesList:
		tile.t.setx(tile.t.xcor() + 20)

def right():
	for tile in tilesList:
		tile.t.setx(tile.t.xcor() - 20)

# Keybinds for scrolling
wn.onkeypress(up, 'Up')
wn.onkeypress(down, 'Down')
wn.onkeypress(left, 'Left')
wn.onkeypress(right, 'Right')

def game(*args):

	while True:
		wn.update()

		for b in btns:
			b.write_text()

try:
	game()

except (TclError, turtle.Terminator):
	pass;

# THERE SHOULD BE NO MAINLOOP HERE