import turtle

from Textures import *

# List of buttons, in case needed later
btns = []

# The window def itself is here because
# it used to be in main and raised lots
# of circular import errors.
wn = turtle.Screen()

# Class for on-screen buttons
class Button():
	# (NOTE: width and height are in pixels, multiplied by 20)
	# There are two parts - an invisible turtle that writes the text, (self.i)
	# and a visible turtle that is the box and registers clicks (self.t).
	def __init__(self, x, y, width, height, wn, texture):

		# Setup
		self.t = turtle.Turtle(); self.t.speed(0); self.t.penup(); self.t.goto(x, y)

		# Main drawing
		self.t.shape('square'); self.t.shapesize(stretch_len = width, stretch_wid = height)

		self.wid = width; self.x = x; self.y = y

		# Texture
		wn.addshape(texture); self.t.shape(texture)

		btns.append(self)

	# Function binding for buttons
	def left_click_bind(self, fun):
		self.t.onclick(fun)

	def right_click_bind(self, fun):
		self.t.onclick(fun, btn = 3)

	# Getting rid of the button
	def hide(self):
		self.t.goto(1000, 1000); self.i.goto(1000, 1000)

# Key is coors, value is tile
tilesDict = {}

# No need for find_tile anymore, because of the dict

# Terrain colors for tiles
# Will replace with textures later
textureDict = {
	'mountain':'Textures/mountains.gif', 'fertile':'Textures/fertile-plains.gif', 'water':'Textures/ocean.gif', 'forest':'Textures/forest.gif',
	'plains':'Textures/plains.gif', 'high': 'Textures/high-mountains.gif', 'deep':'Textures/deep-ocean.gif', 'desert': 'Textures/desert.gif'
}

# This allows the screen to use the textures
def load_texts():
	for tex in textureDict.values():

		# This 'adds' the shape for use by the window
		wn.addshape(tex)

# For creating the game board
class Tile():
	# Tiles have a terrain, position, and belonging units (also turtles, later.)
	def __init__(self, terrain, position, wn):
		self.t = turtle.Turtle()
		self.t.speed(0) # Instant movement
		self.t.penup() # Not drawing lines
		self.t.shape('square');
		self.t.shapesize(stretch_len = 5, stretch_wid = 5)
		self.t.goto(position[0]*110, position[1]*110) # Note that *110 is 20*5 (size) + 10 (border)
		self.p = position

		# tilesDict stores all the tiles with coors as key
		# because all the tiles don't really have names.
		tilesDict[tuple(self.p)] = self; self.tr = terrain; self.t.shape('square')

class TileField():
	# To create a large field of tiles - 'reading' from map.
	def __init__(self, size, wmap): # Size is doubled plus one
		for i in range(-size, size+1):
			for j in range(-size, size+1):

				# Gonna admit right now - this line is REALLY shaky, but will improve later
				# CLOSED: improved with tileDict
				new = Tile(wmap[(i, j)], [i, j], wn)

# For moving all units
unitsList = []

# And now - creation of units
class Unit():
	def __init__(self, maxHP, attack, defense, reach, mobility):
		self.HP = maxHP; self.a = attack; self.d = defense; self.r = reach; self.l = mobility; self.m = maxHP

		unitsList.append(self)

	# Rendering
	def spawn(self, x, y):
		self.t = turtle.Turtle()
		self.t.shape('square'); self.t.penup(); self.t.speed(0)
		self.t.goto(x*110, y*110)
		self.coors = [x, y]

	# Common methods, might add more later
	def attack(self, other):
		other.HP -= self.a/other.d

	def die(self):
		del self

	def heal(self):
		self.HP = self.m

# Unit stats
from troopstats import *

# Dirty lil' trick for init_lands
from level_gen import radius

# Game state system
class GameState():

	# Will store the amount of coins, the tiles owned, the tiles seen, and the current units/positions
	def __init__(self, wealth, owned, vis, unitDict):
		self.w = 10
		self.ts = []
		self.o = []
		self.v = []
		self.u = {}

	# Coors is a list
	def init_lands(self, centerCoors):
		self.ts = self.o = self.u = [tile for tile in radius(centerCoors, 1.5)]
