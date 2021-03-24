# Disjoint Union

Implementation of the union find algorithm. This library will work with all hashable objects.

# Installation

## PyPI

```bash
python3 -m pip install disjoint_union
```

# Usage
`DisjointUnion` is a subclass of `list` and can be instantiated by passing it an iterable. 

You can use the `|` and `+` operators on a `DisjointUnion` to create a new `DisjointUnion`, or you can mutate the original union using the `|=` and `+=` assignment operators, or the `union(x, y)` and `unions(*iterable)` methods. 

```python3
In [1]: from disjoint_union import DisjointUnion
In [2]: d = DisjointUnion(range(5))
In [3]: d
Out[3]: [{0, 1, 2, 3, 4}]

In [4]: d | range(6, 10)
Out[4]: [{0, 1, 2, 3, 4}, {6, 7, 8, 9}]

In [5]: d |= range(6, 10)
In [6]: d
Out[6]: [{0, 1, 2, 3, 4}, {6, 7, 8, 9}]

In [7]: d.union(2, 5)
Out[7]: [{0, 1, 2, 3, 4, 5}, {6, 7, 8, 9}]

In [8]: d |= (5, 6)
In [9]: d
Out[9]: [{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}]

In [10]: d |= range(10, 15)
In [11]: d
Out[11]: [{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {10, 11, 12, 13, 14}]

In [12]: d | (9, 10, 15)
Out[12]: [{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}]
```

