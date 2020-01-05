from classdefs import tilesDict

# 'Scrolling' in all directions
def up():
	for tile in tilesDict.values():
		tile.t.sety(tile.t.ycor() - 20) # It's minus because only the screen is 'going up'

def down():
	for tile in tilesDict.values():
		tile.t.sety(tile.t.ycor() + 20)

def left():
	for tile in tilesDict.values():
		tile.t.setx(tile.t.xcor() + 20)

def right():
	for tile in tilesDict.values():
		tile.t.setx(tile.t.xcor() - 20)

def init_binds(wn):
	# Keybinds for scrolling
	wn.onkeypress(up, 'Up')
	wn.onkeypress(down, 'Down')
	wn.onkeypress(left, 'Left')
	wn.onkeypress(right, 'Right')