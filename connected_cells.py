__author__ = 'alex'
from pprint import pprint
from random import getrandbits, choice

def main():
	pass

def new_connected_set(members):
	return set({member for member in members})

def process_grid(input):
	true_cells = set({})
	input = input.split()
	for y_index, row in enumerate(input):
		processed = process_row(row)
		if processed:
			for x_index in processed:
				true_cells.add((x_index, y_index))
	return true_cells


def process_row(input):
	true_cells = set({})
	input = list(input)
	try:
		while input.index('1') >= 0:
			index = input.index('1')
			true_cells.add(index)
			input[index] = 0
	except ValueError:
		return true_cells


def get_neighbors(pt, true_pts, include_self=True):
	neighbors = set()
	for possible_neighbor in true_pts:
		if not include_self and pt == possible_neighbor:
			continue
		x1, y1 = pt[0], pt[1]
		x2, y2 = possible_neighbor[0], possible_neighbor[1]
		x_diff, y_diff = abs(x1 - x2), abs(y1 - y2)
		if 0 <= x_diff <= 1 and 0 <= y_diff <= 1:
			neighbors.add(possible_neighbor)
	return neighbors

def determine_neighborhood(true_pts):
	return {pt: get_neighbors(pt, true_pts) for pt in true_pts}

def get_groups(intersections):
	pts = intersections.keys()
	pools = []
	for key in intersections.keys():
		for neighbors in intersections.values():
			if not pools:
				pools.append(neighbors)
				continue
			in_these_pools = []
			for pool_id, pool in enumerate(pools):
				if bool(neighbors & pool):
					in_these_pools.append(pool_id)


			if in_these_pools:
				in_these_pools = sorted(in_these_pools, reverse=True)
				new_pool = set({})
				for id in in_these_pools:
					new_pool |= pools[id]
				for id in in_these_pools:
					pools.pop(id)
				pools.append(new_pool)
			else:
				pools.append(neighbors)
	return pools


def gen_examples(max_size=1009, force_size=False):
	min_size = 6
	interval = [value for value in xrange(min_size, max_size)]
	while True:
		if force_size:
			size = max_size
		else:
			size = choice(interval)
		yield size, '\n'.join([''.join([str(getrandbits(1)) for x in xrange(size)]) for y in xrange(size)])




def process_stream(stream):
	for size, example in stream:
		pprint(example)
		true_pts = process_grid(example)
		neighborhood = determine_neighborhood(true_pts)
		#pprint(neighborhood)
		pprint(len(get_groups(neighborhood)))




def main():

	examples = \
		["0010\n1010\n0100\n1111",
		"""1 0 0 1 1
			0 0 1 0 0
			0 0 0 0 0
			1 1 1 1 1
			0 0 0 0 0""",
			"""1 0 0 1 1
			0 0 1 0 0
			0 0 0 0 0
			1 1 1 1 1
			0 0 0 0 0""",
			"""0 0 1 0 0 1 0 0
			1 0 0 0 0 0 0 1
			0 0 1 0 0 1 0 1
			0 1 0 0 0 1 0 0
			1 0 0 0 0 0 0 0
			0 0 1 1 0 1 1 0
			1 0 1 1 0 1 1 0
			0 0 0 0 0 0 0 0"""]

	process_stream(examples)
	s = gen_examples(max_size=8)

	process_stream(s)







if __name__ == "__main__":
	main()