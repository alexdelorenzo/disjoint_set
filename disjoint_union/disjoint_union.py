from typing import Optional, Union, Any, List
from collections import Iterable, Sequence


Iterables = Union[Iterable, Sequence]


class DisjointUnion(list):
    def __init__(self, initial: Optional[Iterable] = None):
        super().__init__()

        if initial is None:
            self |= set()

        else:
            self |= initial

    def __or__(self, other: Iterable) -> 'DisjointUnion':
        return self.unions(other)

    def __ror__(self, other: Iterable) -> 'DisjointUnion':
        return self.__or__(other)

    def __ior__(self, other: Iterable) -> 'DisjointUnion':
        return self.__or__(other)

    def __add__(self, other: Iterable) -> 'DisjointUnion':
        return self.__or__(other)

    def __radd__(self, other: Iterable) -> 'DisjointUnion':
        return self.__add__(other)

    def __iadd__(self, other: Iterable) -> 'DisjointUnion':
        return self.__add__(other)

    def _is_hashable(self, item: Any) -> bool:
        try:
            hash(item)

        except Exception as e:
            return False

        return True

    def _is_iter(self, item: Any) -> bool:
        iters = Iterables.__args__
        is_iter = isinstance(item, iters)

        return is_iter

    def find(self, item: Any) -> Optional[int]:
        for index, pool in enumerate(self):
            if item in pool:
                return index

        return None

    def union(self, x: Any, y: Any) -> 'DisjointUnion':
        x_root, y_root = self.find(x), self.find(y)

        x_present = x_root is not None
        y_present = y_root is not None

        same_root = x_root == y_root
        both_present = x_present and y_present
        one_present = x_present or y_present

        if same_root and both_present:
            pass

        elif both_present:
            xlen, ylen = len(self[x_root]), len(self[y_root])
            sml_x = xlen <= ylen

            sml = x_root if sml_x else y_root
            lrg = y_root if sml_x else x_root

            self[lrg] |= self[sml]
            self.pop(sml)

        elif one_present:
            index = x_root if x_present else y_root
            new_value = y if x in self[index] else x
            self[index].add(new_value)

        else:
            self.append({x, y})

        return self

    def union_iterable(self, iterable: Iterable) -> 'DisjointUnion':
        if isinstance(iterable, str):
            return self.union(iterable, iterable)

        is_hashable = self._is_hashable(iterable)
        is_iterable = self._is_iter(iterable)

        if is_hashable and not is_iterable:
            return self.union(iterable, iterable)

        elif is_iterable:
            iterable = set(iterable)

        length = len(iterable)
        single_item = length is 1
        many_items = length > 1

        if single_item:
            self.append(iterable)

        elif many_items:
            initial = iterable.pop()

            for item in iterable:
                self.union(initial, item)

        return self

    def unions(self, *many_items: List[Any]) -> 'DisjointUnion':
        single_item = len(many_items) is 1

        if single_item:
            many_items = many_items[0]

        return self.union_iterable(many_items)
