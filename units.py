# For moving all units
unitsList = []

# And now - creation of units
class Unit():

	# player is a GameState
	def __init__(self, maxHP, attack, defense, reach, mobility, city):
		self.HP = maxHP; self.a = attack; self.d = defense; self.r = reach; self.l = mobility; self.m = maxHP

		unitsList.append(self)

		self.bar = None

		# If it has already moved in a given turn or not
		self.moved = False

	# Rendering
	# city is a City() object.
	def spawn(self, player, city, cost):
		self.t = turtle.Turtle()
		self.t.shape('square'); self.t.penup(); self.t.speed(0)

		# Textures are 50 wide, 75 tall
		self.t.shapesize(stretch_len = 2, stretch_wid = 3)

		self.t.goto(city.loc[0]*110, city.loc[1]*110)
		self.coors = [x, y]

		self.player = player
		self.city = city

		self.player.w -= cost

		# For partial reimbursement later
		self.cost = cost

	def die(self, reimbursement):
		del self

		if reimbursement:
			self.player.w += self.cost//3

	def attack(self, other):

		# try in case other.d is 0
		try:
			other.HP -= self.a/other.d
		except ZeroDivisionError:
			other.die()

		# Checking for death
		if other.HP <= 0:
			other.die()

	def heal(self):
		self.HP = self.m

	# Cost without barracks
	def incur_cost(self):
		if self.bar is not None:
			self.player.w -= 1

	def move(self, coors):
		if self.moved == False:
			self.t.goto(tile[0]*110, tile[1]*110)
			self.moved = True

''' NOTE: Stats go in order
	maxHP, attack, defense, reach, mobility.
	So the entire file will go in this format

	class UnitType(Unit):
		def __init__(self):
			super().__init__(a, b, c, d, e) '''

# Basic reach and mobility.
class BasicUnit(Unit):
	def __init__(self, maxHP, attack, defense):
		super().__init__(maxHP, attack, defense, 1, 1)

class Soldier(BasicUnit):
	def __init__(self):
		super().__init__(10, 5, 1)

class Swordsman(BasicUnit):
	def __init__(self):
		super().__init__(10, 10, 1)

class Berserker(BasicUnit):
	def __init__(self):
		super().__init__(5, 12, 0.8)

class Shieldman(BasicUnit):
	def __init__(self):
		super().__init__(15, 2, 3)

# Archers, catapults, spearmen and pikemen
# Noice the lowered defense
class WeakRanged(Unit):
	def __init__(self, maxHP, attack, reach):
		super().__init__(maxHP, attack, 0.8, reach, 1)

class Archer(WeakRanged):
	def __init__(self):
		super().__init__(10, 4, 2)

class Catapult(WeakRanged):
	def __init__(self):
		super().__init__(8, 10, 3)

class Spearman(WeakRanged):
	def __init__(self):
		super().__init__(10, 8, 2)

class Pikeman(WeakRanged):
	def __init__(self):
		super().__init__(12, 6, 3)
