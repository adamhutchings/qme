import turtle
import random
import math
from _tkinter import TclError

# Window boilerplate
wn = turtle.Screen()
wn.title('Questionable means of Exploration')
wn.setup(height = 800, width = 800)
wn.bgcolor('#464646'); wn.listen(); wn.tracer(0)

# Exiting
wn.onkeypress(turtle.bye, 'Escape')

# Detecting clicks
lastClick = [None, None]

# Class for on-screen buttons
class Button():
	# (NOTE: width and height are in pixels, multiplied by 20)
	def __init__(self, x, y, width, height, buttonColor, outlineColor, textColor, text):
		self.t = turtle.Turtle(); self.t.color(outlineColor); self.t.speed(0); self.t.penup(); self.t.hideturtle()

		# Drawing the button
		self.t.fillcolor(buttonColor); self.t.begin_fill()

		# Actual drawing
		self.t.goto(x - width*10, y - height*10)
		self.t.width(5); self.t.pendown() # Thickness of line
		self.t.setx(x + width*10); self.t.sety(y + height*10); self.t.setx(x - width*10); self.t.sety(y - height*10)

		self.t.end_fill(); self.t.penup()

		# Writing text (NOTE: Font size is based on the length of the text, and the ycor is based off of the font)
		self.t.color(textColor)
		try:
			fsize = (int((40*width/len(text))//1))
		except ZeroDivisionError:
			raise ValueError('Sorry, your text is empty.')
		self.t.goto(x+2, y - fsize/2)
		self.t.write(text, align = 'center', font = ('Times', fsize, 'bold'))

	# As for key, 1 is left, 2 is middle, and 3 is right. (These are ints, not strs.)
	def bind_func(self, func, key):
		self.t.onclick(func, btn = key)

basicButton = Button(0, 200, 5, 3, '#00FF00', '#FF0000', '#0000FF', 'Hello, World!')

try:
	while True:
		wn.update()
except (TclError, turtle.Terminator):
	pass