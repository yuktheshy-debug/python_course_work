Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#list
l = []
l = list()
type(l)
<class 'list'>
#hetero means it contain all kinds of data
l = [1,12,34,56,'yuk','king',(1,2,3),(5,6,7),{1 : 3, yuk : 56},3+8j]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l = [1,12,34,56,'yuk','king',(1,2,3),(5,6,7),{1 : 3, yuk : 56},3+8j]
NameError: name 'yuk' is not defined
l = [1,12,34,56,"yuk","king",(1,2,3),(5,6,7),{1 : 3, yuk : 56},3+8j]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l = [1,12,34,56,"yuk","king",(1,2,3),(5,6,7),{1 : 3, yuk : 56},3+8j]
NameError: name 'yuk' is not defined
l = [1, 112, 34, "str",True,(1,2,3),{1 : 3, 3 : 4}]
l
[1, 112, 34, 'str', True, (1, 2, 3), {1: 3, 3: 4}]
l = [1,1,1,1]
l
[1, 1, 1, 1]
a = [1,2,3]
b = [4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a = [567,76,13,233,134,234]
a
[567, 76, 13, 233, 134, 234]
a[1]
76
a[0]
567
a[-1]
234
a[-5]
76
a[::2]
[567, 13, 134]
a[:2]
[567, 76]
a[::1]
[567, 76, 13, 233, 134, 234]
a[1:4]
[76, 13, 233]
a[::-1]
[234, 134, 233, 13, 76, 567]
a[1::2]
[76, 233, 234]
a
[567, 76, 13, 233, 134, 234]
76 in a
True
76 not in a
False
12 in a
False
#we can add, we can modify
#list
max(a)
567
min(a)
13
sorted(a)
[13, 76, 134, 233, 234, 567]
len(a)
6
a
[567, 76, 13, 233, 134, 234]
#modification
a[0] = 56
a
[56, 76, 13, 233, 134, 234]
a[3] = 44
a
[56, 76, 13, 44, 134, 234]
a.append(20)
a
[56, 76, 13, 44, 134, 234, 20]
a.insert(2,30)
a
[56, 76, 30, 13, 44, 134, 234, 20]
a.extend([1,2,3,4])
a
[56, 76, 30, 13, 44, 134, 234, 20, 1, 2, 3, 4]
del a[0]
a
[76, 30, 13, 44, 134, 234, 20, 1, 2, 3, 4]
del a[5]
a
[76, 30, 13, 44, 134, 20, 1, 2, 3, 4]
a.pop()
4
a
[76, 30, 13, 44, 134, 20, 1, 2, 3]
a.pop()
3
a
[76, 30, 13, 44, 134, 20, 1, 2]
a.pop(2)
13
a.pop(5)
1
del a[1:3]
a
[76, 134, 20, 2]
>>> a.remove(20)
>>> a
[76, 134, 2]
>>> a.clear()
>>> a
[]
>>> a = [567,76,13,233,134,234]
>>> a.index(76)
1
>>> a
[567, 76, 13, 233, 134, 234]
>>> a.count(134)
1
>>> a = [1,2,3,4]
>>> a = b
>>> b
[4, 5, 6]
>>> b = a
>>> b
[4, 5, 6]
>>> a = [1,2,3,4]
>>> b = a
>>> b
[1, 2, 3, 4]
>>> b.append(7)
>>> b
[1, 2, 3, 4, 7]
>>> a
[1, 2, 3, 4, 7]
>>> c = a.copy()
>>> c.append(7)
>>> c
[1, 2, 3, 4, 7, 7]
>>> a
[1, 2, 3, 4, 7]
>>> any([1,'',False,[],(),{},set()])
True
>>> any([0,'',False,[],(),{},set()])
False
>>> #any one shoul be true then it return true
>>> #otherwise it gives false
>>> all([1,'',False,[],(),{},set()])
False
>>> #all should be true
>>> sum(a)
17
>>> sorted(a)
[1, 2, 3, 4, 7]
>>> a.sort()
>>> a
[1, 2, 3, 4, 7]
>>> a
[1, 2, 3, 4, 7]
>>> a = [1,2,3,4]
>>> a.sort()
>>> a
[1, 2, 3, 4]
>>> a.reverse()
>>> a
[4, 3, 2, 1]
