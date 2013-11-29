__author__ = 'alex'


class DisjointUnion(list):
	def __init__(self, initial=None):
		if initial is not None:
			self.unions(initial)

	def find(self, item):
		for index, pool in enumerate(self):
			if item in pool:
				return index

		return None


	def union(self, x, y):
		xroot, yroot = self.find(x), self.find(y)

		x_present = xroot is not None
		y_present =	yroot is not None

		same_root = xroot == yroot
		both_present = x_present and y_present
		one_present = x_present or y_present

		if same_root and both_present:
			pass

		elif both_present:
			sml, lrg = sorted((xroot, yroot))

			self[sml] |= self[lrg]
			self.pop(lrg)

		elif one_present:
			index = xroot if x_present else yroot
			new_value = y if x in self[index] else x
			self[index].add(new_value)

		else:
			self.append({x, y})

		return self


	def unions(self, set_or_list):
		length = len(set_or_list)
		if length == 1:
				self.append(set(set_or_list))
		elif length > 1:
			initial = set_or_list.pop()
			for item in set_or_list:
				self.union(initial, item)

		return self


def main():
	a, b, c, d = {1,2,3}, {4,5,6,7,8,9}, {'a', 'b', 0}, None
	s = DisjointUnion(a).unions(b).unions(c).union(d, d)
	print(s)
	s.unions({0, 1, 4})
	print(s)



if __name__ == "__main__":
	main()
