Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
t = ()
t = tuple()
t = (1,2,3)
t
(1, 2, 3)
t (1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t (1)
TypeError: 'tuple' object is not callable
t = (1)
t
1
t = (1,) #you need to add comma to print two values
t
(1,)
t = (1,1,1,1) #allows duplicates
t
(1, 1, 1, 1)
type(t)
<class 'tuple'>
#collection of char enclosed bw parenthesis
#ordered,hetero
t = (1,23.4,'str',[1,23], (1,2,3),{1,2,3},{1:1,2:2},True)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
#it is immutable and can store diff kind of data (hetero)
(1,2,3) + (4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3) + (4,5,6) #concatenation
(1, 2, 3, 4, 5, 6)
(1,2,3) * 3 #repetition
(1, 2, 3, 1, 2, 3, 1, 2, 3)
t [1] #indexing
23.4
t [4]
(1, 2, 3)
t [-3]
{1, 2, 3}
t[3 : 7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t [:: -1] #slicing
(True, {1: 1, 2: 2}, {1, 2, 3}, (1, 2, 3), [1, 23], 'str', 23.4, 1)
t [-1 : -4]
()
23.4 in t
True
'str' in t #membership
True
'u' in t
False
'9' is not in t
SyntaxError: invalid syntax
'str is not in t
SyntaxError: unterminated string literal (detected at line 1)
'str' is not in t
SyntaxError: invalid syntax
'str' not in t
False
#these are all operations
sorted(t)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
t = (1,2,3,4,5)
sorted(t)
[1, 2, 3, 4, 5]
len(t)
5
max(t)
5
min (t)
1
t.index(4)
3
t.append(5)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t.append(5)
AttributeError: 'tuple' object has no attribute 'append'
t.count(5)
1
all((1,2,3))
True
any((1,2,3))
True
any((1,2,3,00,000))
True
all((1,2,3,4,00,000))
False
 t = 1,2,3
 
SyntaxError: unexpected indent
t = 1,2,3
sum(t)
6
#packing and unpacking
t= 1,2,3
a,b,c = t
t
(1, 2, 3)
a
1
b
2
c
3
t[4]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    t[4]
IndexError: tuple index out of range
t= 1,2,3,4
t[4]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    t[4]
IndexError: tuple index out of range
t= 1,2,3,4,5,6
t[4]
5
t[4].append(5)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    t[4].append(5)
AttributeError: 'int' object has no attribute 'append'
t = 1,2,3,4, [1, 2, 3], 5
t[4]
[1, 2, 3]
t[4].append(5)
t
(1, 2, 3, 4, [1, 2, 3, 5], 5)
#set
#mut unord uniq dyn hetero
s = {}
type(s)
<class 'dict'>
s = set()
type9s)
SyntaxError: unmatched ')'
type (s)
<class 'set'>
s = {1,2,3,4,5,6,13456,124,43567,312}
s
{1, 2, 3, 4, 5, 6, 43567, 13456, 312, 124}
s = {1,1,1,1}
s
{1}
s = set()
s.add()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s.add(1)
s.add(12.3)
s.add('str')
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({121 : 234})
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s.add({121 : 234})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add((2,3,4))
s.add(False)
s
{False, 1, 12.3, 'str', (2, 3, 4)}
a = {1,2,3,4,5}
b = {3,5,7,8,9}
2 in a
True
10 not in a
True
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
#union - removes the duplicates
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a & b
{3, 5}
#gives the commmon elem
a - b #removes the comon
{1, 2, 4}

#above one is diff
a ^ b #symmetric diff
{1, 2, 4, 7, 8, 9}
#removes the common
a
{1, 2, 3, 4, 5}
#{1}{1,2}{1,2,3,5}, {1,2,3,4,5}, {4,5}{4,5,6}
#subset
a>=b
False
{1,2,}>=a
False
{1,2}>=a
False
a<={4}
False
a<={1,2,3,4,5}
True
m = {1,2,3}
n = {4,5,6}
n.isdisjoint(m)
True
a.disjoint(m)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.disjoint(m)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
#these are the oper we have
a = {12,43,1,7,89,40,23,44}
a
{1, 7, 40, 43, 12, 44, 23, 89}
sorted(a)
[1, 7, 12, 23, 40, 43, 44, 89]
max(a)
89
min(a)
1
len(a)
8
a.index(a)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
a.add(5)
a
{1, 5, 7, 40, 43, 12, 44, 23, 89}
a.find(12)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a.find(12)
AttributeError: 'set' object has no attribute 'find'
a.count(4)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a.count(4)
AttributeError: 'set' object has no attribute 'count'
all({1,1,23,43,13,1})
True
>>> any({0,''})
False
>>> any({0,'',()})
False
>>> any({0,'',(),True})
True
>>> sum(a)
264
>>> a
{1, 5, 7, 40, 43, 12, 44, 23, 89}
>>> a = {1,2,3}
>>> b = a
>>> b.add(4)
>>> b
{1, 2, 3, 4}
>>> a
{1, 2, 3, 4}
>>> #both will be effected
>>> c = a.copy()
>>> c
{1, 2, 3, 4}
>>> a
{1, 2, 3, 4}
>>> c.add(5)
>>> c
{1, 2, 3, 4, 5}
>>> a
{1, 2, 3, 4}
>>> a.add(5)
>>> a
{1, 2, 3, 4, 5}
>>> #for single ele
>>> a.update({10,23,45})
>>> a
{1, 2, 3, 4, 5, 10, 45, 23}
>>> #for adding multiple ele
>>> a
{1, 2, 3, 4, 5, 10, 45, 23}
>>> a.pop()
1
>>> a.pop()
2
>>> a.remove(5)
>>> a
{3, 4, 10, 45, 23}
>>> a.discard(45)
>>> a
{3, 4, 10, 23}
>>> a.discard(45)
>>> a
{3, 4, 10, 23}
>>> #it wont shows error
>>> a.clear()
>>> a
set()
>>> #frozen set is immutable set
>>> a = frozenset({1,2,3})
>>> a
frozenset({1, 2, 3})
>>> #we cannot add and del
