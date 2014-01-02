disjoint_set
============

union find / disjoint union set

usage
===========
```python
In [1]: from disjoint_union import DisjointUnion

In [2]: a, b, c, d = {1,2,3}, {4,5,6,7,8,9}, {'a', 'b', 0}, None

In [3]: s = DisjointUnion(a).unions(b).unions(c).union(d, d)

In [4]: print(s)
[{1, 2, 3}, {4, 5, 6, 7, 8, 9}, {0, 'a', 'b'}, {None}]

In [5]: s.unions({0, 1, 4})
Out[5]: [set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b']), set([None])]

In [6]: print(s)
[{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b'}, {None}]

In [7]: x, y, z = ValueError, 'lol if youre reading this', {x for x in range(90, 80, -1)}

In [8]: s += x

In [9]: s |= {'four', 'score'}

In [10]: print(s)
[{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b'}, {None}, {<class 'ValueError'>}, {'four', 'score'}]


In [11]: ('!@#$' + (s + x) + y) | ( {22,44} | z)
Out[11]: 
[set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'y', 'd', 'e', 'f', 'g', ' ', 'a', 'b', 'l', 't', 'n', 'o', 'h', 'i', 'r', 's', 'u']),
 set([None]),
 set([builtins.ValueError]),
 set(['four', 'score']),
 set(['$', '@', '!', '#']),
 set([22, 44, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90])]

In [12]: print(s)
[{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'y', 'd', 'e', 'f', 'g', ' ', 'a', 'b', 'l', 't', 'n', 'o', 'h', 'i', 'r', 's', 'u'}, {None}, {<class 'ValueError'>}, {'four', 'score'}, {'$', '@', '!', '#'}, {22, 44, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90}]
[14]: [set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'b', 'a']), set([None])]
```

