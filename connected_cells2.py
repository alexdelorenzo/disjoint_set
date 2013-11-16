# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
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

def get_groups(intersections, second_pass=False, pools=[]):
	pts = intersections.keys()

	if second_pass:
		iterate_over = pools
	else:
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
	if not second_pass:
		pools = get_groups(intersections, second_pass=True, pools=pools)
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
		print len(get_groups(neighborhood))

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