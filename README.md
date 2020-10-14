# Disjoint Union

Implementation of the union find algorithm.

# Installation

## PyPI

```bash
python3 -m pip install disjoint_union
```

# Usage

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

In [9]: s | (9, 10)                   
Out[9]: [{0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}]

```

