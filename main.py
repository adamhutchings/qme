import turtle
import random
import math
from _tkinter import TclError

# Other module imports
from classdefs import Button, btns, Tile, tilesList, TileField
from level_gen import mkworld
from scrolling import init_binds

# Window boilerplate
wn = turtle.Screen()
wn.title('Loading...')
wn.setup(height = 800, width = 800)
wn.bgcolor('#464646'); wn.listen(); wn.tracer(0)

# Exiting
wn.onkeypress(turtle.bye, 'Escape')

# Tiles
WORLD_SIZE = 20
world = TileField(WORLD_SIZE, mkworld(WORLD_SIZE))
wn.title('Questionable means of exploration')

init_binds(wn)

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