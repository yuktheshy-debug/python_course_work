Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#TYPE CONVERSIONS
a = 10
float (a)
10.0
str(a)
'10'
complex(a)
(10+0j)
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
b = 10.0
float (b)
10.0
str (b)
'10.0'
complex(b)
(10+0j)
bool(b)
True
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
c = 'yukthesh'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
ValueError: could not convert string to float: 'yukthesh'
str(c)
'yukthesh'
complex(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex(c)
ValueError: complex() arg is a malformed string
bool(c)
True
list(c)
['y', 'u', 'k', 't', 'h', 'e', 's', 'h']
tuple(c)
('y', 'u', 'k', 't', 'h', 'e', 's', 'h')
dict(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
set(c)
{'t', 'h', 'y', 'u', 'e', 's', 'k'}
d = (10+0j)
float(d)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'complex'
str(d)
'(10+0j)'
complex(d)
(10+0j)
bool(d)
True
list(d)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list(d)
TypeError: 'complex' object is not iterable
tuple(d)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    tuple(d)
TypeError: 'complex' object is not iterable
dict(d)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(d)
TypeError: 'complex' object is not iterable
set(d)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    set(d)
TypeError: 'complex' object is not iterable
a = True
float(a)
1.0
str(a)
'True'
complex(a)
(1+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
l = [1, 2, 3, 4 , 5]
float(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
'[1, 2, 3, 4, 5]'
complex(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
tuple(l)
(1, 2, 3, 4, 5)
dict(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
set(l)
{1, 2, 3, 4, 5}
t = (1, 2, 1, 1, 3)
float(t)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> str(t)
'(1, 2, 1, 1, 3)'
>>> complex(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
>>> list(t)
[1, 2, 1, 1, 3]
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> set(t)
{1, 2, 3}
>>> d = {'KYE : 11', 'FYP : 78'}
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'set'
>>> str(d)
"{'FYP : 78', 'KYE : 11'}"
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not set
>>> list(d)
['FYP : 78', 'KYE : 11']
>>> tuple(d)
('FYP : 78', 'KYE : 11')
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 8; 2 is required
>>> set(d)
{'FYP : 78', 'KYE : 11'}
>>> s = {1, 'a', 2, 4}
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
>>> str(s)
"{1, 2, 'a', 4}"
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not set
>>> list(s)
[1, 2, 'a', 4]
>>> tuple(s)
(1, 2, 'a', 4)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> set(s)
{1, 2, 'a', 4}
