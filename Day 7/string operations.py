Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#strip is for first and last
s = '    Hello   world     '
s.strip()
'Hello   world'
s.rstrip()
'    Hello   world'
#removes right space
s.lstrip() #removes left strip
'Hello   world     '
s.replace('  ', '')
'Hello world '
#splitting and joint methods
s = 'pyhon-java-sql'
s.split('-')
['pyhon', 'java', 'sql']
s.split('-',2)
['pyhon', 'java', 'sql']
s.rsplit('-',2)
['pyhon', 'java', 'sql']
s.split('-')
['pyhon', 'java', 'sql']
s.split('-', 1)
['pyhon', 'java-sql']
l = '''python'''
l = '''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
s = ['python', 'java', 'mysql', 'flask']
s
['python', 'java', 'mysql', 'flask']
''.join(s)
'pythonjavamysqlflask'
'  '.join(s)
'python  java  mysql  flask'
', '.join(s)
'python, java, mysql, flask'
'@'.join(s)
'python@java@mysql@flask'
'-'.join(('1','2','3'))
'1-2-3'
"-'.joim(('1','2','3'))
SyntaxError: unterminated string literal (detected at line 1)
'-'.join(('1','2','3'))
'1-2-3'
>>> a = 'strings.py'
>>> a.partition('.')
('strings', '.', 'py')
>>> a = 'string.py.java.png.txt'
>>> a
'string.py.java.png.txt'
>>> a.rpartition('.')
('string.py.java.png', '.', 'txt')
>>> a = 'strings.py'
>>> a.startswith('str')
True
>>> a.endswith('py')
True
>>> a.startswith('oo')
False
>>> 'python.13.islower
SyntaxError: unterminated string literal (detected at line 1)
>>> 'python.13'.islower()
True
>>> 'PYTHON13'.isupper()
True
>>> 'PYTHON13@'.isupper()
True
>>> '123456'.isalnum()
True
>>> 'yegfvbqeh'.isalpha()
True
>>> '517476@'.isalnum()
False
>>> 'Helloworld'.istitle()
True
>>> 'ygfufvu@'.isalpha()
False
>>> '       '.isspace()
True
>>> '  '.isspace()
True
>>> 'my_var'.isisdentifier()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    'my_var'.isisdentifier()
AttributeError: 'str' object has no attribute 'isisdentifier'. Did you mean: 'isidentifier'?
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> '2537135'.isdecimal()
True
>>> 'euwug2352'.isdecimal()
False
>>> '12345'.isdigit()
True
>>> '9876'.isnumerics()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    '9876'.isnumerics()
AttributeError: 'str' object has no attribute 'isnumerics'. Did you mean: 'isnumeric'?
>>> '9876'.isnumeric()
True
