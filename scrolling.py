from units import unitsList
from tiles import tilesDict

# 'Scrolling' in all directions

# The directions are inverted from
# what one might expect because
# everything moving down, for
# example, gives the impression
# that the screen is moving up.

def up():
	for tile in tilesDict.values():
		tile.t.sety(tile.t.ycor() - 20)
	for unit in unitsList:
		unit.t.sety(unit.t.ycor() - 20)

def down():
	for tile in tilesDict.values():
		tile.t.sety(tile.t.ycor() + 20)
	for unit in unitsList:
		unit.t.sety(unit.t.ycor() + 20)

def left():
	for tile in tilesDict.values():
		tile.t.setx(tile.t.xcor() + 20)
	for unit in unitsList:
		unit.t.setx(unit.t.xcor() + 20)

def right():
	for tile in tilesDict.values():
		tile.t.setx(tile.t.xcor() - 20)
	for unit in unitsList:
		unit.t.setx(unit.t.xcor() - 20)

def init_binds(wn):
	# Keybinds for scrolling
	wn.onkeypress(up, 'Up')
	wn.onkeypress(down, 'Down')
	wn.onkeypress(left, 'Left')
	wn.onkeypress(right, 'Right')