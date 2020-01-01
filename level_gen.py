# This is for creating fields of tiles

import random
import math

final_output = {}

tileTypes = ['mountain', 'water', 'plains', 'forest', 'fertile', 'high', 'deep', 'desert']

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

fadeLevels = {'mountain': 6, 'water': 1.5, 'forest': 3, 'plains': 2.5,
'fertile':5, 'high':10, 'deep':2.5, 'desert':3.5}

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

	# Making deep water shallow next to land
	for tile in final_output.keys():
		if final_output[tile] == 'deep':
			for other in radius(tile, 1.5):
				if final_output[other] not in ['deep', 'water']:
					final_output[tile] = 'water'

	# Making shallow water deep far away from land
	for tile in final_output.keys():
		if final_output[tile] == 'water':
			oc = True
			for other in radius(tile, 3):
				if final_output[other] not in ['deep', 'water']:
					oc = False

			if oc:
				final_output[tile] = 'deep'

def mkworld(size):
	start_world(size); create_centers(size); spread(); complete()

	# Making sure the world is well balanced

	# How many of each tile type there are
	tCounts = {}
	for tType in tileTypes:
		tCounts[tType] = 0

	for tile in final_output:
		tCounts[final_output[tile]] += 1

	size = len(final_output.keys())

	if tCounts['mountain'] + tCounts['high'] > size/8:
		for tile in final_output.keys():
			if final_output[tile] == 'mountain' or final_output[tile] == 'high':
				final_output[tile] = random.choice(['plains', 'fertile', 'water', 'mountain'])

	if tCounts['water'] + tCounts['deep'] > size*2/3:
		for tile in final_output:
			if final_output[tile] in ['water', 'deep']:
				if random.randrange(1, 30) == 5:
					for other in radius(tile, 1.5):
						if final_output[other] in ['water', 'deep']:
							final_output[other] = random.choice(['plains', 'forest', 'desert'])

	return final_output
