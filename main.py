import turtle
import random
import math
from _tkinter import TclError

# Other module imports
from classdefs import Button, btns

# Window boilerplate
wn = turtle.Screen()
wn.title('Questionable means of exploration')
wn.setup(height = 800, width = 800)
wn.bgcolor('#464646'); wn.listen(); wn.tracer(0)

# Exiting
wn.onkeypress(turtle.bye, 'Escape')

def game(*args):

	while True:
		wn.update()

		for b in btns:
			b.write_text()

try:
	game()

except (TclError, turtle.Terminator):
	pass;

wn.mainloop()