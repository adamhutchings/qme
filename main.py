import turtle
import random
import math

# Window boilerplate
wn = turtle.Screen()
wn.title('Questionable means of Exploration')
wn.setup(height = 800, width = 800)
wn.bgcolor('#824736'); wn.listen(); wn.tracer(0)

# Exiting
wn.onkeypress(turtle.bye, 'Escape')

# For writing things
pen = turtle.Turtle()
pen.hideturtle(); pen.penup()
pen.write('QME', align = 'center', font = ('Times', 50, 'normal'))

while True:
	wn.update()