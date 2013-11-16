from random import getrandbits, choice
from itertools import repeat


def process_grid(input):
	nodes = set({})
	input = input.split()
	for y_index, row in enumerate(input):
		processed = process_row(row)
		if processed:
			for x_index in processed:
				nodes.add((x_index, y_index))
	return nodes


def process_row(input):
	nodes = set({})
	input = list(input)
	try:
		while input.index('1') >= 0:
			index = input.index('1')
			nodes.add(index)
			input[index] = 0
	except ValueError:
		return nodes


#def get_neighbors(pt, nodes, include_self=True, interval=[(x,y) for x in xrange(-1,2) for y in xrange(-1,2)]):
#	neighbors = set()
#	x1, y1 = pt
#	for x2, y2 in nodes:
#		x_diff, y_diff = x1 - x2, y1 - y2
#		if -1 <= x_diff <= 1 and -1 <= y_diff <= 1:
#			neighbors.add((x2,y2))
#	#neighbors.remove(pt)
#	#neighbors = [(x1 + x2, y1 + y2) for y1, y2 in interval]
#
#	return neighbors

def get_neighbors(pt, nodes, i=[(x,y) for x in xrange(-1,2) for y in xrange(-1,2)]):
	x1, y1 = pt
	neighbors =  (  (x1 + x2, y1 + y2) for x2, y2 in i  )
	return {neighbor for neighbor in neighbors if neighbor in nodes}


def determine_neighborhood(true_pts):
	return {pt: get_neighbors(pt, true_pts) for pt in true_pts}

def _get_groups(intersections, second_pass=False, pools=[]):
	pts = intersections.keys()

	#if second_pass:
	#	iterate_over = intersections
	#else:
	iterate_over = intersections.keys()
	for iterate in iterate_over:
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
					pools.pop(id)
				pools.append(new_pool)
			else:
				pools.append(neighbors)
	#if not second_pass:
	#	pools = get_groups(intersections, second_pass=True, pools=pools)
	return pools

def get_groups(intersections):
	pts = intersections.keys()
	pools = []
	for passes in xrange(2):
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
					pools.pop(id)
				pools.append(new_pool)
			else:
				pools.append(neighbors)
	return pools

def rtn_example(size=8):
	return '\n'.join([''.join([str(getrandbits(1)) for x in xrange(size)]) for y in xrange(size)])

def gen_examples(max_size=1009, force_size=False):
	min_size = 6
	interval = [value for value in xrange(min_size, max_size)]
	while True:
		if force_size:
			size = max_size
		else:
			size = choice(interval)
		yield size, rtn_example(size)




def process_stream(stream):
	for size, example in stream:
		#pprint(example)
		true_pts = process_grid(example)
		neighborhood = determine_neighborhood(true_pts)
		#pprint(neighborhood)
		print size, len(get_groups(neighborhood))

def main():
	from sys import stdin
	from pprint import pprint

	stdin = open('/home/alex/Desktop/input00.txt', 'r')
	list_in = [line.strip('\n').replace(" ", "") for line in stdin.readlines()]
	test_cases = int(list_in.pop(0))
	frames = []
	while len(frames) < test_cases:
	    size = int(list_in.pop(0))
	    frame = '\n'.join(list_in[:size])
	    #print size, frame
	    frames.append((size, frame))
	    list_in = list_in[size:]

	process_stream(frames)
	process_stream(gen_examples(max_size=100))

if __name__ == "__main__":
	main()