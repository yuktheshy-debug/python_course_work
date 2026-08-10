Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> 
=========================================================== RESTART: /Users/yuktheshgayakawada/Desktop/PYTHON 65 /Day 2/variable operations.py ===========================================================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a = 10
>>> b = 20
>>> a
10
>>> b
20
>>> a = b = c = 10
>>> a =
SyntaxError: invalid syntax
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c = 10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a = 10
>>> b = 20
>>> a,b = b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a
NameError: name 'a' is not defined
