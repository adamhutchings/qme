import turtle
import random
import math
from _tkinter import TclError

# Other module imports
from classdefs import Button

# Window boilerplate
wn = turtle.Screen()
wn.title('Questionable means of Exploration')
wn.setup(height = 800, width = 800)
wn.bgcolor('#464646'); wn.listen(); wn.tracer(0)

# Exiting
wn.onkeypress(turtle.bye, 'Escape')

basicButton = Button(0, 200, 5, 3, '#FF0000', '#00FF00', 'Hello, World!')

try:
	while True:
		wn.update()

		# Need to loop or else gets written over.
		basicButton.write_text('Hello, World!', '#00FF00')
except (TclError, turtle.Terminator):
	pass