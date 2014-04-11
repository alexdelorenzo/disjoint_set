disjoint_set
============

union find / disjoint union set

usage
===========
```python
In [1]: from disjoint_union import DisjointUnion

In [2]: a, b, c, d, e, f, g = {1,2,3}, {4,5,6}, {'a', 'b', 0}, None, ValueError(), (object, str), str

In [3]: s = DisjointUnion(a)

In [4]: s
Out[4]: [{1, 2, 3}]

In [5]: s.unions(b).unions(c).union(d, d)
Out[5]: [{1, 2, 3}, {4, 5, 6}, {'b', 0, 'a'}, {None}]

In [6]: s.unions('test', 22, 55, 99)
Out[6]: [{1, 2, 3}, {4, 5, 6}, {'b', 0, 'a'}, {None}, {99, 'test', 22, 55}]

In [7]: s.union(22, 77)
Out[7]: [{1, 2, 3}, {4, 5, 6}, {'b', 0, 'a'}, {None}, {99, 'test', 77, 22, 55}]

In [8]: s + 66
Out[8]: [{1, 2, 3}, {4, 5, 6}, {'b', 0, 'a'}, {None}, {99, 'test', 77, 22, 55}, {66}]

In [9]: s.union(66, 22)
Out[9]: [{1, 2, 3}, {4, 5, 6}, {'b', 0, 'a'}, {None}, {22, 55, 66, 77, 99, 'test'}]

In [11]: s |= f

In [12]: s
Out[12]:
[{1, 2, 3},
 {4, 5, 6},
 {'b', 0, 'a'},
 {None},
 {22, 55, 66, 77, 99, 'test'},
 {builtins.object, builtins.str}]

In [13]: ('!@#$' + (s + g) + 'hey there') | ( {22,44} | set('char set'))
Out[13]:
[{1, 2, 3}, {4, 5, 6}, {0, 66, 99, 'h', 77, 'e', 'a', 'test', 44, ' ', 'c', 'b', 22, 55, 't', 's', 'r'}, {None}, {<class 'object'>, <class 'str'>}, {'!@#$'}, {'hey there'}]

 In [14]: s.unions(1, 4, 22, None, 's', str)
Out[14]:
[{'b', 1, 2, 3, 4, 5, 6, 'c', ' ', 'h', None, 77, 'r', 's', 'a', 66, 't', 'test', 22, 0, 99, <class 'object'>, 'e', 44, <class 'str'>, 55}, {'!@#$'}, {'hey there'}]

```

