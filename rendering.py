# This is a program to optimize rendering time, and the output is
# one complete rendering cycle.

# Imports
from classdefs import Tile, tilesDict, textureDict

# Key is tile place, value is image used
tileImageDict = {}

for tile in tilesDict.values():

	# Square is the default shape
	tileImageDict[tile] = 'square'

def in_screen(tile):
	if (tile.t.xcor() < -400 or tile.t.xcor() > 400) and (tile.t.ycor() < -400 or tile.t.ycor() > 400):
		return False

	return True

def update_texts():
	for tile in tileImageDict.values():
		if in_screen(tile):

			# Not updating the image if we don't have to

			# If the texture is blank
			if tileImageDict[tile] == 'square':

				# Updating the image, both in-dict and in-turtle
				tileImageDict[tile] = textureDict[tile.tr]; tile.t.shape(textureDict[tile.tr])

		else:
			if tileImageDict[tile] != 'square':
				tileImageDict[tile] = 'square'; tile.t.shape('square')