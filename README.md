# Disjoint Union

Implementation of the union find algorithm. This library will work with any hashable objects.

# Installation

## PyPI

```bash
python3 -m pip install disjoint_union
```

# Usage
`DisjointUnion` is a subclass of `list` and can be instantiated by passing it an iterable. You can use the pipe methods `|` & `|=` as well as the `union(x, y)` and `unions(*iterable)` methods.

```python3
In [1]: from disjoint_union import DisjointUnion                            
In [2]: s = DisjointUnion(range(3))   

In [3]: s                             
Out[3]: [{0, 1, 2}]

In [5]: s.unions(range(6, 10))        
Out[5]: [{0, 1, 2}, {6, 7, 8, 9}]

In [6]: s.union(2, 5)                 
Out[6]: [{0, 1, 2, 5}, {6, 7, 8, 9}]

In [7]: s.union(5, 6)                 
Out[7]: [{0, 1, 2, 5, 6, 7, 8, 9}]

In [8]: s | range(10, 15)             
Out[8]: [{0, 1, 2, 5, 6, 7, 8, 9}, {10, 11, 12, 13, 14}]

In [9]: s | (9, 10, 15)                   
Out[9]: [{0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}]

```

