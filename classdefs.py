import turtle

# Class for on-screen buttons
class Button():
	# (NOTE: width and height are in pixels, multiplied by 20)
	# There are two parts - an invisible turtle that writes the text, (self.i)
	# and a visible turtle that is the box and registers clicks (self.t).
	def __init__(self, x, y, width, height, buttonColor):

		# Setup
		self.t = turtle.Turtle(); self.t.speed(0); self.t.penup(); self.t.goto(x, y)

		# Main drawing
		self.t.shape('square'); self.t.shapesize(stretch_len = width, stretch_wid = height); self.t.color(buttonColor)

		self.wid = width; self.x = x; self.y = y

	def write_text(self, text, textColor):
		# Turtle to write the text
		self.i = turtle.Turtle(); self.i.speed(0); self.i.hideturtle(); self.i.penup()

		# Text
		fontSize = int(40*self.wid/len(text)//1)

		self.i.goto(self.x, self.y - fontSize/2)
		self.i.color(textColor); self.i.write(text, align = 'center', font = ('Times', fontSize, 'bold'))

	def click_bind(self, fun):
		self.t.onclick(fun)