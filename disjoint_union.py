__author__ = 'alex'


class DisjointUnion(list):
	def __init__(self, initial={}):
		if initial:
			self.append(initial)

	def find(self, item):
		for index, pool in enumerate(self):
			if item in pool:
				return {index}

		return None


	def union(self, x, y):
		xroot, yroot = self.find(x), self.find(y)

		both_equal, both_present, one_present = \
			xroot == yroot, xroot and yroot, xroot or yroot

		if both_equal and both_present:
			pass

		elif both_present:
			sml, lrg = sorted((xroot.pop(), yroot.pop()))

			self[sml] |= self[lrg]
			self.pop(lrg)

		elif one_present:
			index = one_present.pop()
			new_value = y if x in self[index] else x
			self[index].add(new_value)

		else:
			self.append({x, y})

		return self


	def unions(self, set_or_list):
		length = len(set_or_list)
		if length == 1:
				self.append({item for item in set_or_list})
		elif length > 1:
			initial = set_or_list.pop()
			for item in set_or_list:
				self.union(initial, item)

		return self


def main():
	a, b, c, d = {1,2,3}, {4,5,6,7,8,9}, {'a', 'b', 3}, None
	s = DisjointUnion(a).unions(b).unions(c).union(d, 0)
	print(s)
	s.unions({0, 1, 4})
	print(s)



if __name__ == "__main__":
	main()