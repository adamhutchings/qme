import turtle

btns = []

# Class for on-screen buttons
class Button():
	# (NOTE: width and height are in pixels, multiplied by 20)
	# There are two parts - an invisible turtle that writes the text, (self.i)
	# and a visible turtle that is the box and registers clicks (self.t).
	def __init__(self, x, y, width, height, buttonColor, text, textColor):

		# Setup
		self.t = turtle.Turtle(); self.t.speed(0); self.t.penup(); self.t.goto(x, y)

		# Main drawing
		self.t.shape('square'); self.t.shapesize(stretch_len = width, stretch_wid = height); self.t.color(buttonColor)

		self.wid = width; self.x = x; self.y = y

		btns.append(self)

		self.text = text; self.tc = textColor

	def write_text(self):
		# Turtle to write the text
		self.i = turtle.Turtle(); self.i.speed(0); self.i.hideturtle(); self.i.penup()

		# Text
		fontSize = int(40*self.wid/len(self.text)//1)

		self.i.goto(self.x, self.y - fontSize/2)
		self.i.color(self.tc); self.i.write(self.text, align = 'center', font = ('Times', fontSize, 'bold'))

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
	'mountain':'#b5651d', 'plains':'#22bf03', 'water':'#1188d3', 'forest':'#116f23'
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
