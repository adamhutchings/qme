import turtle

# For error handling at the end (stupid tkinter)
from _tkinter import TclError

# Other module imports
from classdefs import *
from scrolling import init_binds
from rendering import *
from troopstats import *

# Window boilerplate
wn.title('Loading...')
wn.setup(height = 800, width = 800)
wn.bgcolor('#464646') # Dark gray
wn.listen()
wn.tracer(0) # So we can control window updates manually

# Exiting
wn.onkeypress(turtle.bye, 'Escape')

# Tiles
WORLD_SIZE = 20
# World size is actually WORLD_SIZE*2 + 1, so
# this world is actually 41 tiles across.

world = TileField(WORLD_SIZE, mkworld(WORLD_SIZE))
wn.title('Questionable means of exploration')

# Scrolling
init_binds(wn)

# Textures
load_image_dict()
load_texts()

# Init game states
playerState = GameState(10)
playerState.init_lands([0, 0])

# Making the global game state
tGame = GlobalGameState([playerState], world)

def game():

	while True:
		wn.update()

		# Updating textures
		update_texts()

		# Add more things here later for the main game loop

# Error handling 
try:
	game()

# These errors that happen
except (TclError, turtle.Terminator):
	pass;

# THERE SHOULD BE NO MAINLOOP HERE