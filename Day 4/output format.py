Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #outputformat
>>> #comma separation format
>>> a = 10
>>> b = 12.3
>>> c = 'codegnan'
>>> print(a, b, c)
10 12.3 codegnan
>>> print("a=",a, "b=", b, "c=', c)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("a=",a, "b=", b, 'c=', c)
...       
a= 10 b= 12.3 c= codegnan
>>> print("a=",a, "b=", b, 'c=', c, sep='')
...       
a=10b=12.3c=codegnan
>>> print("a=",a, "b=", b, 'c=', c, sep='\n')#for next line
...       
a=
10
b=
12.3
c=
codegnan
>>> print("a=",a, "b=", b, 'c=', c, sep='\t')#for tab space
...       
a=	10	b=	12.3	c=	codegnan
>>> print("a=",a, "b=", b, 'c=', c, sep='\n\n')#for two lines or extra line
...       
a=

10

b=

12.3

c=

codegnan
>>> print("a=",a, "b=", b, 'c=', c, sep='\t', end='\n\n')#for to lines
...       
a=	10	b=	12.3	c=	codegnan

>>> #or to end with two libnes
...       
>>> print("a=",a, "b=", b, 'c=', c, sep='\t', end='@')#for tab space
...       
a=	10	b=	12.3	c=	codegnan@
>>> print(f'a=(a) b=(b) c(c)')
...       
a=(a) b=(b) c(c)
>>> print{f'a=(a) b=(b) c(c)'}
...       
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(f'a={a} b={b} c{c}')
...       
a=10 b=12.3 ccodegnan
>>> #f' string is the recommended one
      
print(f'a=%d b=%f c=%s'%(a, b, c))')
      
SyntaxError: unterminated string literal (detected at line 1)
print(f'a=%d b=%f c=%s'%(a, b, c))
      
a=10 b=12.300000 c=codegnan
print('a=() b=() c=()' .format(a, b, c))
      
a=() b=() c=()
print('a=() b=() c=()' .format (b,c,a))
      
a=() b=() c=()
