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
	def __init__(self, x, y, width, height, color):
		self.t = turtle.Turtle(); self.t.color(color)
		self.t.penup(); self.t.speed(0)
		self.t.goto(x, y)
		self.t.shape('square'); self.t.shapesize(stretch_len = width, stretch_wid = height)

	# As for key, 1 is left, 2 is middle, and 3 is right. (These are ints, not strs.)
	def bind_func(self, func, key):
		self.t.onclick(func, btn = key)

basicButton = Button(0, 300, 5, 2, '#ffffff')

try:
	while True:
		wn.update()
except (TclError, turtle.Terminator):
	pass