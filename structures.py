# This is for all sorts of structures.
# Specifics decided later.

import turtle
from level_gen import radius

class Structure():

	def __init__(self, texture, location, wn):
		self.t = turtle.Turtle()
		self.t.penup();
		self.t.goto(location[0], location[1])
		self.t.shape(texture)

		self.loc = location

	def destroy(self):
		del self

class City(Structure):

	def __init__(self, location, spread, wn, owner):
		super().__init__('Textures/City/city.gif', location, wn)

		# For stats about the city

		# The level of size
		self.level = 1

		# How close it is to next level
		self.fillbar = 0

		# Territories
		# For how radius works, see level_gen.py
		self.terr = radius(location, spread)

		self.owner = owner

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

class Farm(Structure):

	# Farms produce 2 food for the city.
	# Keep in mind that food is used sending
	# away troops.

	def __init__(self, texture, location, wn, belongCity):
		super().__init__(texture, location, wn)

		self.city = belongCity

class Barracks(Structure):

	# Barracks house units on the move and
	# can be grown into a city. Units on the
	# move without barracksn cost 1 resource per
	# turn.

	def __init__(self, texture, location, wn, units):
		super().__init__(texture, location, wn)
		self.u = units

		# Letting units know that they have a barracks
		for unit in self.u:
			unit.bar = self

class Port(Structure):

	def __init__(self, texture, location, wn, belongCity):
		super().__init__(texture, location, wn)
		self.city = belongCity
		self.city.fillbar(3)

class Mine(Structure):

	def __init__(self, texture, location, wn, belongCity):
		duper().__init__(texture, location, wn)
		self.city = belongCity

	def give_coins(self):
		self.city.owner.w += 3