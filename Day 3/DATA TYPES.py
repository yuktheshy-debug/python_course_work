Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#data types
#int float complex

a = 12
type (a)
<class 'int'>
b = 22.3
type (b)
<class 'float'>
c = 12+3j
type (c)
<class 'complex'>
#sequential data types
#str list tuple
#string is a collection of char bw enclosed '' , cannoot change it is immutable
s = 'Codegnan'
id(s)
4470821360
s += 'Python'
s
'CodegnanPython'
id(s)
4374826608
s = 'aaaaaa'
s
'aaaaaa'
type(s)
<class 'str'>
#list is a collection of ele bw enclosed and it is mutable
l = [1, 2, 3, 4]
type (l)
<class 'list'>
>>> id(l)
4374402880
>>> l.append(5)
>>> l
[1, 2, 3, 4, 5]
>>> id(l)
4374402880
>>> heterogeneous (can contain diff data types,dynamically sized,allow duplivcates,mutable,ordered)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> #heterogeneous (can contain diff data types,dynamically sized,allow duplivcates,mutable,ordered)
>>> i = [1, 2, 3, 'str', 5]
>>> typr(i)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    typr(i)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> type(i)
<class 'list'>
>>> #tuple is a collection of ele bw enclosed braces
>>> t = (1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
>>> t = (1, 2, 3, 4)
>>> t
(1, 2, 3, 4)
>>> t = (1, 2, 'str', 4)
>>> type(t)
<class 'tuple'>
>>> t
(1, 2, 'str', 4)
>>> #immutable, ordered, hetero,fixed size, allow dupli
>>> #enclosed vth parenthesis ()
>>> #Mapping data types
>>> #set : set is a collection of ele bw curly braces
>>> #mutable, doesntvallow duplicates, dynamically sixed, hetero, unordered
>>> s = {1, 2, 3, 4}
>>> type (s)
<class 'set'>
>>> id(s)
4470156512
>>> s.add(21)
>>> s
{1, 2, 3, 4, 21}
>>> s = {1, 2, 'a', 4}
>>> type(s)
<class 'set'>
>>> s
{1, 2, 'a', 4}
>>> #dictionary is a collection of ele bw curly braces {}
>>> d = {'pro', 'KYE', 'pric': 876, 'stock': True}
SyntaxError: invalid syntax
>>> #mutable, ordered, dynamically sized, hetero
>>> #frozen  set is similar to the SET
>>> s = frozen set{1, 1, 1, 2, 4}
SyntaxError: invalid syntax
>>> s = frozenset{1, 2, 1, 2, 4}
SyntaxError: invalid syntax
>>> s = frozenset({1, 2, 1, 1, 3})
>>> s
frozenset({1, 2, 3})
>>> type(s)
<class 'frozenset'>
>>> #bulean
>>> #mutale data types : list set dictionary
>>> #Type converions
>>> a = 10
>>> float(a)
10.0
>>> #bulean : other than zero TRUE, if it is zero FALSE
