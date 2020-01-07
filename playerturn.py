# This module will provide functions for the
# main.py to use during a player turn

# To init binds for all units
from classdefs import unitsList, buttonsList, Unit

# This is technically to check if tiles
# are in the screen, but because tiles
# and units both have a .t method, it
# also works for units.
from rendering import in_screen

# Global selectedUnit
selectedUnit = None

def select_unit(unit):

	# When a unit is selected, it moves up slightly
	# on the screen to show its being selected
	unit.t.sety(unit.t.ycor() + 10)

def change_selection(oldUnit, newUnit):

	# Moves old unit down and new unit up.
	select_unit(newUnit)
	oldUnit.t.sety(oldUnit.t.ycor() - 10)

def unit_info(unit):

	# Will add later - draws up something
	# with info about the unit.

	# Triggered by clicking the selected
	# unit - see move_unit() for specifics.

	pass

def click_in_unit(x, y, unit):
	# Checking if clicks are in square shape of unit
	# Keep in mind that the units are 40 wide
	# and 60 tall, so 20 and 30 away from
	# the middle of the unit
	# click coors are specified by x, y

	return (x > unit.t.xcor() - 20 and x < unit.t.xcor() + 20) and (y > unit.t.ycor() - 30 and y < unit.t.ycor() + 30)

def click_in_tile(x, y, tile):

	# Same as above, but tiles are 100x100.
	return (x > unit.t.xcor() - 50 and x < unit.t.xcor() + 50) and (y > unit.t.ycor() - 50 and y < unit.t.ycor() + 50)

# This function is to detect if a
# unit was clicked and then make that
# unit the selected one.
def switch_selection(x, y):

	# I didn't make this a function arg
	# because onscreenclick() takes in
	# two coordinate args.
	global selectedUnit

	for unit in unitsList:

		# Don't bother if units are outside screen
		if click_in_unit(x, y, unit) and in_screen(unit):

			selectedUnit = unit
			return None

# This attacks a chosen unit
def attack_unit(x, y):

	global selectedUnit

	for unit in unitsList:

		if click_in_unit(x, y, unit) and in_screen(unit):

			# Bringing up unit info
			if unit == selected_unit:
				unit_info(unit)

			else:

				# Make the attack
				selectedUnit.attack(unit)

def move_unit(x, y):

	global selectedUnit

	for unit in unitsList:

		# One unit can't move atop another
		if click_in_unit(x, y, unit) and in_screen(unit):

			# Just stop all other checking (same below too)
			return None

	for tile in tilesList:
		if click_in_tile(x, y, tile) and in_screen(tile):

			# Undocument the below later, when
			# an allowed_moves list func is built

			''' if tile in allowed_moves(selectedUnit):'''

			selectedUnit.t.goto(tile.t.xcor(), tile.t.ycor())
			return None

def player_turn(wn):

	global selectedUnit

	# Which unit the player has selected
	selectedUnit = None

	# Detecting clicks

	# The arguments passed to the event handlers
	# are the coors of the click.
	# btn is which key (1 is left), add adds a new binding
	# rather than replacing an old one.
	wn.onscreenclick(switch_selection, btn=1, add=True)
	wn.onscreenclick(attack_unit, btn=1, add=True)
	wn.onscreenclick(move_unit, btn=3, add=True)
