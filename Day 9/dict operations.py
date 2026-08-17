Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#dict is a collection of key val pairs enclosed bw {}
#mut ord het dyn uniq dupl
d = {}
type(d)
<class 'dict'>
d = {1 : 1}
d
{1: 1}
d = {}
d[1] = 1
d[2] = 12.3
d[[3] = 'str'
  
SyntaxError: invalid syntax
d[3] = 'str'
  
d[4] = 2+3j
  
d[5] = ([1,2,3])
  
d[12.3] = 1
  
d["str"] = 1
  
d [(1,2,3)] = 1
  
d[ (2+3j) ] = 1
  
d[True] = 1
  
d[[1,2,3]] = 1
  
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[[1,2,3]] = 1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d [ {1,2,3} ] = 1
  
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d [ {1,2,3} ] = 1
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[1] = 1
  
d
  
{1: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: [1, 2, 3], 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1}
d[2] = 1
  
d
  
{1: 1, 2: 1, 3: 'str', 4: (2+3j), 5: [1, 2, 3], 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1}
d[3] = 5
  
d
  
{1: 1, 2: 1, 3: 5, 4: (2+3j), 5: [1, 2, 3], 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1}
d[1] = 1
  
d[2] =2
  
d[3] ='str'
  
d[4] = 2+3j
  
d[5] = True
  
d[6] = [1,2,3]
  
d[7] = (1,2,3)
  
d[8] = {1,2,3}
  
d[9] = frozenset((1,2,3))
  
d[10] ={1:1,2:2}
  
d[11] = None
  
d
  
{1: 1, 2: 2, 3: 'str', 4: (2+3j), 5: True, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 2}, 11: None}
#values may be duplicates but keys should be uniq
  
d = {}
  
d[1] = 2
  
d
  
{1: 2}
d[1] = 3
  
d
  
{1: 3}
#keys must be uniq
  
#vth the help of keys we can access thye value
  
#member and accessing only two dict oper
  
data = {'name' : 'yukthesh', 'course'  : 'python', 'batch' : '65'}
  
data
  
{'name': 'yukthesh', 'course': 'python', 'batch': '65'}
data[name]
  
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    data[name]
NameError: name 'name' is not defined
data.get('name')
  
'yukthesh'
data['name']
  
'yukthesh'
data['batch']
  
'65'
data['age']
  
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    data['age']
KeyError: 'age'
#we also have another met
  

data.get('name')
  
'yukthesh'
data.get('batch')
  
'65'
data.get('age','key is not present')
  
'key is not present'
data.get('batch','key is not present')
  
'65'
#exceptional handling
  
#to add single ele data['phnno']
  
data['phnno'] = 9876543210
  
d
  
{1: 3}
data
  
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210}
data.update({'email' : 'yukthesh@gmail.com'})
  
data
  
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com'}
#this is for adding single ele
  
data
  
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com'}
data.update({}) #is for adding multiple ele
  
data.popitem()
  
('email', 'yukthesh@gmail.com')
data
  
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210}
#last ele will be removed
  
data.pop({'phnno'})
  
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    data.pop({'phnno'})
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
data['py']
  
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    data['py']
KeyError: 'py'
data['phnno']
  
9876543210
data['phnno'] = 6788766788
  
data
  
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 6788766788}
#it will update the key
  
data['batch'] = 76
  
data
  
{'name': 'yukthesh', 'course': 'python', 'batch': 76, 'phnno': 6788766788}
data.pop('course')
  
'python'
data
  
{'name': 'yukthesh', 'batch': 76, 'phnno': 6788766788}
#to pop a part item
  
data.pop('batch')
  
76
dtaa
  
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    dtaa
NameError: name 'dtaa' is not defined
data
  
{'name': 'yukthesh', 'phnno': 6788766788}
del data['batch']
  
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    del data['batch']
KeyError: 'batch'
del data['name']
  
data
  
{'phnno': 6788766788}
data
  
{'phnno': 6788766788}
l = {'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com'}
  
del l['course']
  
l
  
{'name': 'yukthesh', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com'}
data.clear()
  
l
  
{'name': 'yukthesh', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com'}
data.clear()
  
data
  
{}
l.clear()
  
l
  
{}
data ={'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com'}
  
len(data)
  
5
data.keys()
  
dict_keys(['name', 'course', 'batch', 'phnno', 'email'])
data.value()
  
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    data.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
data.values()
  
dict_values(['yukthesh', 'python', '65', 9876543210, 'yukthesh@gmail.com'])
sorted(data)
  
['batch', 'course', 'email', 'name', 'phnno']
max(data)
  
'phnno'
min(data)
  
'batch'
d = {1,2,3}
  
m = {4,5,6}
  
m = d
  
d
  
{1, 2, 3}
m
  
{1, 2, 3}
c = d.copy()
  
c
  
{1, 2, 3}
d
  
{1, 2, 3}
c = m.copy()
  
c
  
{1, 2, 3}
m
  
{1, 2, 3}
d = {1,2,3}
  
m = {4,5,6,7,8}
  
SyntaxError: multiple statements found while compiling a single statement
d = {1,2,3}
  
m = {7,8,9}
  
SyntaxError: multiple statements found while compiling a single statement
d = {1,2,3}
  
m = {7,8,9}
  
m = d
  
d = {1,2,3}
  
m = {6,7,9}
  
n = m.copy()
  
n
  
{9, 6, 7}
m
  
{9, 6, 7}
n = d.copy()
  
n
  
{1, 2, 3}
d
  
{1, 2, 3}
d = {1:1,2:2}
  
m = d
  
m{3}
...   
SyntaxError: invalid syntax
>>> m[3]
...   
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    m[3]
KeyError: 3
>>> m[3] = 3
...   
>>> m
...   
{1: 1, 2: 2, 3: 3}
>>> d
...   
{1: 1, 2: 2, 3: 3}
>>> n = d.copy()
...   
>>> n[5] = 5
...   
>>> n
...   
{1: 1, 2: 2, 3: 3, 5: 5}
>>> d
...   
{1: 1, 2: 2, 3: 3}
>>> data
...   
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com'}
>>> data.get('py')
...   
>>> data
...   
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com'}
>>> data.setdefault('py',2026)
...   
2026
>>> data
...   
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com', 'py': 2026}
>>> #adds the new value
...   
>>> data.setdefault('age' : 21)
...   
SyntaxError: invalid syntax
>>> data.setdefault('age',21)
...   
21
>>> data
...   
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com', 'py': 2026, 'age': 21}
>>> data.setdefault('key',234)
...   
234
>>> data
...   
{'name': 'yukthesh', 'course': 'python', 'batch': '65', 'phnno': 9876543210, 'email': 'yukthesh@gmail.com', 'py': 2026, 'age': 21, 'key': 234}
>>> dict.fromkeys(["python","mysql","java"],0) #to assign 0 for multiple keys instead of writing "python" : 0 we can use fromkeys
...   
{'python': 0, 'mysql': 0, 'java': 0}
