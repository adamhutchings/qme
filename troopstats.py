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
		super().__init__(15, 0.4, 3)