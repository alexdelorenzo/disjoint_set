from __future__ import annotations
from typing import Any, Hashable
from collections.abc import Iterable, Sequence


Item = Hashable
Items = Iterable[Item]
ItemSet = set[Item]
Iterables = Iterable | Sequence  # don't subscript, used with isinstance()


class DisjointUnion(list[Item]):
  def __init__(self, initial: Items | None = None):
    super().__init__()

    if initial is None:
      self |= set()

    else:
      self |= initial

  def __contains__(self, key: Item) -> bool:
    return self.find(key) is not None

  def __or__(self, other: Items) -> DisjointUnion:
    return self.combine_new(other)

  #def __ror__(self, other: Iterable[Hashable]) -> 'DisjointUnion':
    #return self.__or__(other)

  def __ior__(self, other: Items) -> DisjointUnion:
    if isinstance(other, type(self)):
      self.combine(other)
      return self

    return self.unions(other)

  def __add__(self, other: Items) -> DisjointUnion:
    return self.__or__(other)

  #def __radd__(self, other: Iterable[Hashable]) -> 'DisjointUnion':
    #return self.__add__(other)

  def __iadd__(self, other: Item) -> DisjointUnion:
    return self.__ior__(other)

  def _is_hashable(self, item: Item | Any) -> bool:
    return isinstance(item, Hashable)

  def _is_iter(self, item: Item) -> bool:
    iters = Iterables.__args__
    return isinstance(item, iters)

  def combine(self, other: DisjointUnion):
    for pool in other:
      self |= pool

  def combine_new(self, other: DisjointUnion) -> DisjointUnion:
    if isinstance(other, type(self)):
      return add_unions(self, other)

    return add_items(self, other)

  def copy(self) -> DisjointUnion:
    new = DisjointUnion()

    for pool in self:
      new |= pool

    return new

  def find(self, item: Item) -> int | None:
    for index, pool in enumerate(self):
      if item in pool:
        return index

    return None  # be explicit

  def get_set(self, item: Item) -> ItemSet | None:
    if index := self.find(item) is not None:
      return self[index]

    return None  # be explicit

  def remove(self, item: Item) -> bool:
    if pool := self.get_set(item):
        return False

    pool.remove(item)

    if not pool:
      index = self.index(pool)
      self.pop(index)

    return True

  def union(self, x: Item, y: Item) -> DisjointUnion:
    x_root, y_root = self.find(x), self.find(y)

    x_present = x_root is not None
    y_present = y_root is not None

    same_root = x_root == y_root
    both_present = x_present and y_present
    # one_present = x_present or y_present

    if same_root and both_present:
      pass

    elif both_present:
      xlen, ylen = len(self[x_root]), len(self[y_root])
      sml_x = xlen <= ylen

      sml = x_root if sml_x else y_root
      lrg = y_root if sml_x else x_root

      self[lrg] |= self[sml]
      self.pop(sml)

    elif x_present or y_present:
      index = x_root if x_present else y_root
      new_value = y if x in self[index] else x
      self[index].add(new_value)

    else:
      self.append({x, y})

    return self

  def union_iterable(self, items: Items | Iterable) -> DisjointUnion:
    if isinstance(items, str):
      return self.union(items, items)

    is_hashable = self._is_hashable(items)
    is_iterable = self._is_iter(items)

    if is_hashable and not is_iterable:
      return self.union(items, items)

    elif is_iterable:
      items = set(items)

    length = len(items)
    single_item = length == 1
    # many_items = length > 1

    if single_item:
      self.append(items)

    elif length > 1:
      initial = items.pop()

      for item in items:
        self.union(initial, item)

    return self

  def unions(self, *many_items: tuple[Hashable]) -> DisjointUnion:
    single_item = len(many_items) == 1

    if single_item:
      [many_items] = many_items

    return self.union_iterable(many_items)


def add_unions(d1: DisjointUnion, d2: DisjointUnion) -> DisjointUnion:
  new = d1.copy()

  for pool in d2:
    new |= pool

  return new


def add_items(union: DisjointUnion, items: Items) -> DisjointUnion:
  new = union.copy()
  new |= items

  return new
