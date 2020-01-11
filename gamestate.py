# Dirty lil' trick for init_lands
from level_gen import radius

# Game state system per player
class GameState():

	# Will store the amount of coins, the tiles owned, the tiles seen, and the current units/positions
	def __init__(self, wealth):
		self.w = wealth # Money
		self.o = [] # Tiles owned
		self.v = [] # Tiles visible
		self.u = {} # unitDict

	# Coors is a list
	def init_lands(self, centerCoors):
		self.o = self.u = [tile for tile in radius(centerCoors, 1.5)]

# Total game state
class GlobalGameState():

	# Stores the tilesList, which units are where, and some GameState objects.
	def __init__(self, gameStates, world):
		self.tiles = world
		self.unitsDict = {}
		self.gameStateList = gameStates
