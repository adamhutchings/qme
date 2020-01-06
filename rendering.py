# This is a program to optimize rendering time, and the output is
# one complete rendering cycle.

# Imports
from classdefs import Tile, tilesDict, textureDict

# Key is tile place, value is image used
tileImageDict = {}

# First-pass putting every tile in the image dict
def load_image_dict():
	for tile in tilesDict.values():

		# Square is the default shape
		tileImageDict[tile] = 'square'

# 450, not 400, so edge tiles still render
def in_screen(tile):
	if (tile.t.xcor() < -450 or tile.t.xcor() > 450) and (tile.t.ycor() < -450 or tile.t.ycor() > 450):
		return False

	return True

def update_texts():
	for tile in tileImageDict:
		if in_screen(tile):

			# Not updating the image if we don't have to

			# If the texture is blank
			if tileImageDict[tile] == 'square':

				# Updating the image, both in-dict and in-turtle
				tileImageDict[tile] = textureDict[tile.tr]; tile.t.shape(textureDict[tile.tr])

		else:
			if tileImageDict[tile] != 'square':
				tileImageDict[tile] = 'square'; tile.t.shape('square')
