Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #string operations
>>> #how to declare a string
>>> s = 'yukthesh'
>>> s
'yukthesh'
>>> type(s)
<class 'str'>
>>> s = ''
>>> s
''
>>> a = 'python'
>>> b = 'programming'
>>> a + b
'pythonprogramming'
>>> a+b
'pythonprogramming'
>>> fname = yukthesh
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fname = yukthesh
NameError: name 'yukthesh' is not defined
>>> fname = "yukthesh"
>>> lname = "gaikwad"
>>> fname + lname
'yuktheshgaikwad'
>>> a = python
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a = python
NameError: name 'python' is not defined
>>> a = "python"
>>> a * 10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
>>> '*'*20
'********************'
>>> #concatenation
>>> #repetition
>>> #above examples are of...
>>> #accessing a particular char
>>> #positive and negative indexing
>>> #indexing,slicing,membership
>>> s = 'codegnan'
>>> s[7]
'n'
>>> s[5]
'n'
>>> s[6]
'a'
>>> #positive indexing starts from '0'
>>> s[-1]
'n'
>>> s[-3]
'n'
>>> s[-5]
'e'
>>> #negative indexing starts from left side with '-1'
>>> #slicing
>>> names = 'yukthesh','king','nag'
>>> names[:8]
('yukthesh', 'king', 'nag')
names = 'yukthesh nag king'
names[:8]
'yukthesh'
names[:10]
'yukthesh n'
names[9:11]
'na'
names[9:12]
'nag'
names[-1]
'g'
names[:-2,-5]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    names[:-2,-5]
TypeError: string indices must be integers, not 'tuple'
names[-1:-5]
''
names[-1:-6]
''
names[-1:-7]
''
#a[n,end+1,step]
#membership
'yukthesh' in names
True
'chay' in names
False
'shrey' not in names
True
len(names)
17
ord('h')
104
ord('y')
121
chr(1)
'\x01'
chr(13)
'\r'
chr(5)
'\x05'
sorted(names)
[' ', ' ', 'a', 'e', 'g', 'g', 'h', 'h', 'i', 'k', 'k', 'n', 'n', 's', 't', 'u', 'y']
max(names)
'y'
min(names)
' '
#len(), ord(), chr(), sorted(), max(), min()
#case convertion method
s = 'pyhton programming language'
s.upper() #converts all into uppercase letters
'PYHTON PROGRAMMING LANGUAGE'
s.lower()
'pyhton programming language'
#converts all into small
s.swapcase() #converts low yo upper and upper to lower case letters just opposite
'PYHTON PROGRAMMING LANGUAGE'
s.capitalize() #keeps only first letter as uppercase
'Pyhton programming language'
s.title() #keeps all the first letters of words as uppercase
'Pyhton Programming Language'
WFUVBRIVÂâÅ.casefold()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    WFUVBRIVÂâÅ.casefold()
NameError: name 'WFUVBRIVÂâÅ' is not defined
#casefold()

#allignment methods
s.center(50,'-')
'-----------pyhton programming language------------'
s.center(40,'*')
'******pyhton programming language*******'
s.ljust(40,'-')
'pyhton programming language-------------'
s.rjust(35,'_')
'________pyhton programming language'
'123'.zfill(4)
'0123'
'4567'.zfill(7)
'0004567'
#zfill adds the zeroes in the starting
'658465857'.zfill(2)
'658465857'
#search and find methods
#find is gng to give part value index
#find has exceptional handling
s = 'python programming lang'
s.find('python')
0
s.find('p')
0
s.find('t')
2
s.find('0'0
       
SyntaxError: '(' was never closed
s.find('o')
       
4
s.rfind('p')
       
7
s.rfind('a')
       
20
#index
       
s.index('a')
       
12
s.index('p')
       
0
s.rindex('a')
       
20
# r means it is gng to give right most value
       
s.count('a)
        
SyntaxError: unterminated string literal (detected at line 1)
s.count('a')
        
2
s.count('p')
        
2
#replace is used to replace part set of str
        
s.replace('o', '4')
        
'pyth4n pr4gramming lang'
s.replace('p', '7')
        
'7ython 7rogramming lang'
s.replace('python', 'java')
        
'java programming lang'
s.markettrans('aeiou', '%^&*(')
        
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    s.markettrans('aeiou', '%^&*(')
AttributeError: 'str' object has no attribute 'markettrans'. Did you mean: 'maketrans'?
s.markettrans('aeiou', '%^&*£')
        
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    s.markettrans('aeiou', '%^&*£')
AttributeError: 'str' object has no attribute 'markettrans'. Did you mean: 'maketrans'?
s.maketrans('aeiou', '%^&*(')
        
{97: 37, 101: 94, 105: 38, 111: 42, 117: 40}
s.translate(s.maketrans('aeiou', '%^&*('))
        
'pyth*n pr*gr%mm&ng l%ng'
text = "Hello 😀"
        
text.encode()
        
b'Hello \xf0\x9f\x98\x80'
b'Hello \xf0\x9f\x98\x80'.decode()
        
'Hello 😀'
#encode means convert data into bytes
        
