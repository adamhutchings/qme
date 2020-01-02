import turtle

btns = []

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

# Terrain colors for tiles
# Will replace with textures later
colorDict = {
	'mountain':'#b5651d', 'fertile':'#95a308', 'water':'#1188d3', 'forest':'#116f23',
	'plains':'#55bf03', 'high': '#222222', 'deep':'#08446a', 'desert': '#bfa203'
}

class Tile():
	# Tiles have a terrain, position, and belonging units (also turtles, later.)
	def __init__(self, terrain, position):
		self.t = turtle.Turtle()
		self.t.speed(0); self.t.penup(); self.t.shape('square'); self.t.shapesize(stretch_len = 5, stretch_wid = 5)
		self.t.color(colorDict[terrain]); self.t.goto(position[0]*110, position[1]*110); self.u = None # Note that *110 is 20*5 (size) + 10 (border)

		tilesList.append(self)

class TileField():
	# To create a large field of tiles - 'reading' from map.
	def __init__(self, size, wmap): # Size is doubled plus one
		tileDict = {} # key - coords; value - Tile instance
		for i in range(-size, size+1):
			for j in range(-size, size+1):

				# Gonna admit right now - this line is REALLY shaky, but will improve later
				new = Tile(wmap[(i, j)], [i, j])

# And now - creation of units
class Unit():
	def __init__(self, maxHP, attack, defense):
		self.HP = maxHP; self.a = attack; self.d = defense; self.m = maxHP

	def attack(self, other):
		other.HP -= self.a/other.d

	def die(self):
		del self

	def heal(self):
		self.HP = self.m
