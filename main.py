import turtle
import random
import math
from _tkinter import TclError

# Other module imports
from classdefs import Button, btns, Tile, tilesDict, TileField, wn, load_texts
from level_gen import mkworld
from scrolling import init_binds
from rendering import update_texts

# Window boilerplate
wn.title('Loading...')
wn.setup(height = 800, width = 800)
wn.bgcolor('#464646'); wn.listen(); wn.tracer(0)

# Exiting
wn.onkeypress(turtle.bye, 'Escape')

# Tiles
WORLD_SIZE = 20
world = TileField(WORLD_SIZE, mkworld(WORLD_SIZE))
wn.title('Questionable means of exploration')

# Scrolling
init_binds(wn)

# Textures
load_texts()

# Removed button, now uses textures (NOT TESTED)

def game():

	while True:
		wn.update()

		# Updating textures
		update_texts()

try:
	game()

# These errors that happen
except (TclError, turtle.Terminator):
	pass;

# THERE SHOULD BE NO MAINLOOP HERE