__author__ = 'alex'


class DisjointUnion(list):
	def __init__(self, initial={}):
		self.sets = self
		if initial:
			self.append(initial)

	def find(self, item):
		for index, pool in enumerate(self.sets):
			if item in pool:
				return {index}

		return False

		#return {index for index, pool in enumerate(self.sets) if item in pool}

	def union(self, x, y):
		xroot, yroot = self.find(x), self.find(y)

		both_equal, both_present, one_present = \
			xroot == yroot, xroot and yroot, xroot or yroot

		if both_equal and both_present:
			pass

		elif both_present:
			sml, lrg = sorted((xroot.pop(), yroot.pop()))

			self.sets[sml] |= self.sets[lrg]
			self.sets.pop(lrg)

		elif one_present:
			index = one_present.pop()
			new_value = y if x in self[index] else x
			self.sets[index].add(new_value)

		else:
			self.sets.append({x, y})

		return self


	def unions(self, set_or_list):
		length = len(set_or_list)
		if length == 1:
				self.append({item for item in set_or_list})
				return self
		elif length > 1:
			initial = set_or_list.pop()
			for item in set_or_list:
				self.union(initial, item)

		return self







def main():
	pass


if __name__ == "__main__":
	main()