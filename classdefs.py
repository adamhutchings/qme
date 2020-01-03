import turtle

# For textures - import path doesn't work for some reason
from Textures import *

btns = []

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

	def left_click_bind(self, fun):
		self.t.onclick(fun)

	def right_click_bind(self, fun):
		self.t.onclick(fun, btn = 3)

	# Getting rid of the button
	def hide(self):
		self.t.goto(1000, 1000); self.i.goto(1000, 1000)

tilesList = []

# Finding a tile
# Takes in a list
def find_tile(coors):
	for tile in tilesList:
		if tile.p == coors:
			return tile

# Terrain colors for tiles
# Will replace with textures later
textureDict = {
	'mountain':'mountians.gif', 'fertile':'furtaile-plains.gif', 'water':'ocean.gif', 'forest':'forest.gif',
	'plains':'plains.gif', 'high': 'high-mountains.gif', 'deep':'deep-ocean.gif', 'desert': 'desert.gif'
}

class Tile():
	# Tiles have a terrain, position, and belonging units (also turtles, later.)
	def __init__(self, terrain, position, wn):
		self.t = turtle.Turtle()
		self.t.speed(0); self.t.penup(); self.t.shape('square'); self.t.shapesize(stretch_len = 5, stretch_wid = 5)
		self.t.goto(position[0]*110, position[1]*110); self.u = None # Note that *110 is 20*5 (size) + 10 (border)

		# Textures
		wn.addshape(textureDict[terrain]); self.t.shape(textureDict[terrain]); 

		tilesList.append(self); self.p = position

class TileField():
	# To create a large field of tiles - 'reading' from map.
	def __init__(self, size, wmap): # Size is doubled plus one
		tileDict = {} # key - coords; value - Tile instance
		for i in range(-size, size+1):
			for j in range(-size, size+1):

				# Gonna admit right now - this line is REALLY shaky, but will improve later
				new = Tile(wmap[(i, j)], [i, j], wn)

# And now - creation of units
class Unit():
	def __init__(self, maxHP, attack, defense, reach, mobility):
		self.HP = maxHP; self.a = attack; self.d = defense; self.r = reach; self.l = mobility; self.m = maxHP;

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
