Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#python operators
#arithmetical operators
a = 10
b = 5
a + b
15
a - b
5
a * b
50
a / b
2.0
a / 2
5.0
9 / 2
4.5
9 // 2
4
12 // 2
6
12 / 2
6.0
13 / 2
6.5
13 // 2
6
14 / 2
7.0
15 / 2
7.5
a ** 2
100
2 ** 3
8
16 ** 2
256
12 % 2
0
13 % 2
1
% - reminder
SyntaxError: invalid syntax
#comparision operators
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
a>=10
True
a>=5
True
a>=13
False
#assignment operator
a = 20
a = a+10
a
30
a = a+30
a
60
a += 20
a
80
a -= 20
a
60
a *= 2
a
120
a /= 2
a
60.0

a //= 2
a
30.0

a %= 2
a
0.0
a = 30
a %= 2
a
0
#relational operators
email = True
password = False
email and password
False
#in and both should be true then it give result as TRUE
emaial or password
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    emaial or password
NameError: name 'emaial' is not defined. Did you mean: 'email'?
login = True
login = False
display_products = True
login or display_products
True
login and display_products
False
's' in 'aeiou'
False
's' not in 'aeiou'
True
7%2==0
False
6%2==0
True
7%2==0 and 3%2=0
SyntaxError: cannot assign to expression
7%2==0 and 3%2==0
False
6%2==0 or 3%2==0
True
3%2==0
False
6%2==0
True
not 3%2==0
True

#and (both should be true)
#or(any one should be true)
#str list tuple set dict
s = 'python programming'
'python' in s
True
'programming' in s
True
'pfs' in s
False
'java' not in s
True
'java' in s
False
l = [1, 2, 3, 4]
3 in l
True
5 in l
False
2 not in l
False
3 not in l
False
1 in l
True
#tuple
t = (20, 30, 40, 50)
20 in t
True
60 in t
False
70 not in t
True
40 in t
True
s = {'pen', 'paper' 'book'}
'pen' in s
True
'book' not in s
True
'car' not in s
True
#dict
data = {'name' : 'yukthesh', 'age' : 21'}
        
SyntaxError: unterminated string literal (detected at line 1)
data = {'name' : 'yukthesh', 'age' : '21'}
        
'name' in data
        
True
'name' not in data
        
False
'age' in data
        
True
#it only works for keys not for values
        
'21' in data
        
False
#identity operation
        
#if both are sharing the same obj ref then the result will be true
        
#id should be same then they are IDENTICAL
        
l = [1, 2, 3, 4]
        
m = [1, 2, 3, 4]
        
id(l)
        
4328096448
id(m)
        
4327751808
l is m
        
False
l == m
...         
True
>>> n = m
...         
>>> n
...         
[1, 2, 3, 4]
>>> id(n)
...         
4327751808
>>> m is n
...         
True
>>> m == n
...         
True
>>> n is not m
...         
False

>>> #bitwise operator
...         
>>> 11 & 12
...         
8
>>> & | ^ ~ >> <<
...         
SyntaxError: invalid syntax
>>> #& | ^ ~ >> <<
...         
>>> 11 & 12
...         
8
>>> 11 | 12
...         
15
>>> 11 ^ 12
...         
7
>>> 11 ~ 12
...         
SyntaxError: invalid syntax
>>> 11 >> 12
...         
0
>>> 11 << 12
...         
45056
>>> ~11
...         
-12
>>> ~12
...         
-13
>>> ~45
...         
-46
>>> ~55
...         
-56
