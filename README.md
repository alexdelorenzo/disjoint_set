disjoint_set
============

union find / disjoint union set

usage
===========
```python
In [2]: import disjoint_union as du

In [3]: du.DisjointUnion()
Out[3]: []


In [7]: disjoint_set1, disjoint_set2 = du.DisjointUnion(), du.DisjointUnion({x for x in range(5,10)})


In [9]: disjoint_set2
Out[9]: [set([8, 9, 5, 6, 7])]

In [10]: a, b, c, d = {1,2,3}, {4,5,6,7,8,9}, {'a', 'b', 0}, None

In [11]: disjoint_set1.unions(a).unions(c)
Out[11]: [set([1, 2, 3]), set(['b', 0, 'a'])]

In [12]: disjoint_set1.union(d, d)
Out[12]: [set([1, 2, 3]), set(['b', 0, 'a']), set([None])]

In [13]: disjoint_set1.union(1, 'a')
Out[13]: [set([0, 1, 2, 3, 'b', 'a']), set([None])]

In [14]: disjoint_set1.unions([x for x in range(10)])
Out[14]: [set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'b', 'a']), set([None])]
```



About
============
has nothing to do with the library but why it came about: made counting connected groups easier. unfortunately, i was pretty inefficient in processing a adjancey list from an adjacency grid. now i have homework to finish.
