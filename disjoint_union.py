__author__ = 'alex'


class DisjointUnion(list):
    def __init__(self, initial={}):
        if initial:
            self |= initial

    def __or__(self, other):
        return self.unions(other)

    def __ror__(self, other):
        return self.__or__(other)

    def __add__(self, other):
        return self.__or__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __ior__(self, other):
        return self.__or__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def find(self, item):
        for index, pool in enumerate(self):
            if item in pool:
                return index

        return None

    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)

        x_present = xroot is not None
        y_present = yroot is not None

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

    def union_iterable(self, iterable):
        if isinstance(iterable, str):
            return self.union(iterable, iterable)

        try:
            iterable = set(iterable)

        except TypeError as t_e:
            return self.union(iterable, iterable)

        length = len(iterable)

        if length == 1:
            self.append(iterable)

        elif length > 1:
            initial = iterable.pop()

            for item in iterable:
                self.union(initial, item)

        return self

    def unions(self, *many_items):
        if len(many_items) is 1:
            many_items = many_items[0]

        return self.union_iterable(many_items)


def main():
    a, b, c, d = {1, 2, 3}, {4, 5, 6, 7, 8, 9}, {'a', 'b', 0}, None

    s = DisjointUnion(a).unions(b).unions(c).union(d, d)
    print(s)

    s.unions({0, 1, 4})
    print(s)

    x, y, z = ValueError, 'lol if youre reading this', {x for x in range(90, 80, -1)}

    s += x
    s |= {'four', 'score'}
    print(s)

    ('!@#$' + (s + x) + y) | ( {22, 44} | z)
    print(s)


if __name__ == "__main__":
    main()