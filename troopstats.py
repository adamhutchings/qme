from classdefs import Unit

''' NOTE: Stats go in order
	maxHP, attack, defense, reach, mobility.
	So the entire file will go in this format

	class UnitType(Unit):
		def __init__(self):
			super().__init__(a, b, c, d, e)

	There also migh tbe 'default' inherited classes
	to be code less monotonous.'''

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