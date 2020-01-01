# This is for creating fields of tiles

import random
import math

final_output = {}

tileTypes = ['mountain', 'water', 'plains', 'forest']

def start_world(size):
	for i in range(-size, size+1):
		for j in range(-size, size+1):
			final_output[(i, j)] = None

centers = []

def create_centers(size):
	for tile in final_output:

		# 4% chance of being a center
		if random.randrange(1, 25) == 5:
			centers.append(tile)
			final_output[tile] = random.choice(tileTypes)

def distance(tile1, tile2):
	return math.sqrt((tile1[0] - tile2[0])**2 + (tile1[1] - tile2[1])**2)

# All tiles within a given radius
def radius(tile, dis):
	return [near for near in final_output.keys() if distance(tile, near) < dis]

def nearest_center(tile):
	for dis in range(0, 8):
		for other in radius(tile, dis):
			if other in centers:
				return other

	# If there are no nearby centers
	centers.append(tile); return tile

fadeLevels = {'mountain': 5, 'water': 1, 'forest': 2, 'plains': 2}

# Now, center types spread to nearby tiles
def spread():

	for tile in final_output.keys():

		# Now, the farther away from the center it is, the more likely it is
		# to be a different tile type.

		cen = nearest_center(tile)

		try:
			fade = fadeLevels[final_output[cen]]
		except KeyError:
			final_output[cen] = random.choice(tileTypes); fade = fadeLevels[final_output[cen]]

		if random.randrange(1, 99) < 100 - fade*(distance(tile, cen)):
			final_output[tile] = final_output[cen]
		else:
			final_output[tile] = random.choice(tileTypes)

def complete():
	for tile in final_output.keys():
		if final_output[tile] == None:
			final_output[tile] = random.choice(tileTypes)

	return final_output

def mkworld(size):
	start_world(size); create_centers(size); spread(); complete(); return final_output
