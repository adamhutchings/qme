import turtle

# Key is coors, value is tile
tilesDict = {}

# No need for find_tile anymore, because of the dict

# Terrain colors for tiles
# Will replace with textures later
textureDict = {
	'mountain':'Textures/Terrain/mountains.gif', 'fertile':'Textures/Terrain/fertile-plains.gif',
	'water':'Textures/Terrain/ocean.gif', 'forest':'Textures/Terrain/forest.gif',
	'plains':'Textures/Terrain/plains.gif', 'high': 'Textures/Terrain/high-mountains.gif',
	'deep':'Textures/Terrain/deep-ocean.gif', 'desert': 'Textures/Terrain/desert.gif'
}

# This allows the screen to use the textures
def load_texts(wn):
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
	def __init__(self, size, wmap, wn): # Size is doubled plus one
		for i in range(-size, size+1):
			for j in range(-size, size+1):

				# Gonna admit right now - this line is REALLY shaky, but will improve later
				# CLOSED: improved with tileDict
				new = Tile(wmap[(i, j)], [i, j], wn)

		# Vars for later use
		self.tmap = wmap