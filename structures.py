# This is for all sorts of structures.
# Specifics decided later.

import turtle
from level_gen import radius

class Structure():

	def __init__(self, texture, location, wn):
		self.t = turtle.Turtle()
		self.t.penup();
		self.t.goto(location[0], location[1])
		wn.addshape(texture); self.t.shape(texture)

	def destroy(self):
		del self

class City(Structure):

	def __init__(self, location, spread, wn):
		super().__init__('Textures/City/city.gif', location, wn)

		# For stats about the city

		# The level of size
		self.level = 1

		# How close it is to next level
		self.fillbar = 0

		# Territories
		# For how radius works, see level_gen.py
		self.terr = radius(location, spread)

	def check(self):

		# If it can level up
		while True:

			# This loop decreases the amount until it isn't 'overflowing'.
			if self.fillbar >= self.level:
				self.fillbar -= self.level; self.level += 1
			else:
				break;

	# Add a certain amount of population
	def fill(self, amount):
		self.fillbar += amount

		# To make sure there's no spillover
		self.check()
