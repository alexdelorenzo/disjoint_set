from random import getrandbits, choice
from itertools import repeat
from copy import deepcopy as dc
from disjoint_union import DisjointUnion as du

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


def get_neighbors(pt, nodes):
	i = [(x,y) for x in xrange(-1,2) for y in xrange(-1,2)]
	x1, y1 = pt
	neighbors =  (  (x1 + x2, y1 + y2) for x2, y2 in i  )
	return {neighbor for neighbor in neighbors if neighbor in nodes}


def determine_neighborhood(true_pts):
	return {pt: get_neighbors(pt, true_pts) for pt in true_pts}


def disjoint_sets(intersections):
	disjoint_union = du()

	for key, vals in intersections.iteritems():
		disjoint_union.unions(vals)
	return disjoint_union

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
		print size, len(disjoint_sets(neighborhood))

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
	process_stream(gen_examples(max_size=100, force_size=True))

if __name__ == "__main__":
	main()