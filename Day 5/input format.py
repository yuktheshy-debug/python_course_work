Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #input formatting
>>> #int float complex str list tuple dict set bool
>>> #str as input
>>> #input()
>>> a = input()
a
>>> #str into int int()
>>> #we want to convert str into int, float to take as an input
>>> a = input()
a
>>> a = input("Enter the value : ")
Enter the value : 55
>>> a
'55'
>>> marks = input("Enter the marks : ")
Enter the marks : 33
>>> marks
'33'
>>> marks = int(input("Enter the marks : "))
Enter the marks : 55
>>> marks
55
>>> price = float(input("Enter the price : "))
Enter the price : 66.3
>>> price
66.3
>>> cgpa = float(input("Enter the cgpa : "))
Enter the cgpa : 9.8
>>> cgpa
9.8
>>> #str input()
>>> #int int(input())
>>> #float float(input())
>>> names = 'yukthesh akhil sushanth'
>>> names.split()#split is default means no need to mention space
['yukthesh', 'akhil', 'sushanth']
>>> names = 'yukthesh sushanth akhil akkineni'
>>> names = 'akhil,akkineni,sushanth,yukthesh'
>>> names.split(',')
['akhil', 'akkineni', 'sushanth', 'yukthesh']
>>> courses = 'python-java-sql'
>>> courses.split('-')
['python', 'java', 'sql']
>>> #we just need to mention in the parenthesis
>>> names = 'king nag chay'
>>> names.split()
['king', 'nag', 'chay']
>>> names = input("Enter the names: ").split()
Enter the names: yukthesh akhil king
>>> names
['yukthesh', 'akhil', 'king']
>>> names = tuple(input("Enter the names : ").split())
Enter the names : yukthesh king nag
>>> names
('yukthesh', 'king', 'nag')
>>> names = set(input("Enter the names : ").split())
Enter the names : yukthesh 77 boy
>>> names
{'boy', '77', 'yukthesh'}
names = set(input("Enter the names : ").split('-'))
Enter the names : 'python-java-course'

names
{'java', "'python", "course'"}
#list of integeres
marks = input().split()
marks
marks = '23 54 66 77 88'
marks = input().split()
marks
marks = input("Enter the marks : ").split()
Enter the marks : 23 54 66 77
marks
['23', '54', '66', '77']
map(int,marks)
<map object at 0x103070e80>
list(map(int,marks))
[23, 54, 66, 77]
set(map(int,marks))
{66, 77, 54, 23}
marks = list(map(int,input("Enter the marks : ").split()))
Enter the marks : 22 44 55 66
marks
[22, 44, 55, 66]
marks = set(map(int,input("Enter the marks : ").split()))
Enter the marks : 22 44 55 66
marks
{66, 44, 22, 55}
marks = tuple(map(int,input("Enter the marks : ").split()))
Enter the marks : 22 33 44 55
marks
(22, 33, 44, 55)
marks = set(map(float,input("Enter the marks : ").split()))
Enter the marks : 44.3 55.4 66.3
marks
{66.3, 44.3, 55.4}
marks = tuple(map(float,input("Enter the marks : ").split()))
Enter the marks : 33.3 2.2 3.3
marks
(33.3, 2.2, 3.3)
marks = list(map(float,input("Enter the marks : ").split()))
Enter the marks : 22.2 3.3 4.4
marks
[22.2, 3.3, 4.4]
a, b= [1,2]
a
1
b
2
a,b,c=(1, 12.3, 'str')
a
1
b
12.3
c
'str'
email,password=input("Enter the email,password : ").split()
Enter the email,password : yukthesh@y 2519
email,password
('yukthesh@y', '2519')
name,marks=input("Enter the name and marks : ").split()
Enter the name and marks : yuk 38
name
'yuk'
marks
'38'
int(marks)
38
marks = list(map(int,input("Enter the marks : ").split()))
Enter the marks : 22 55 66 77
marks
[22, 55, 66, 77]
marks = list(map(float,input("Enter the marks : ").split()))
Enter the marks : 2.2 3.3 4.4
marks
[2.2, 3.3, 4.4]
#complex bool dict
#for true and false use eval
status = eval(input())
True
status
True
type(status)
<class 'bool'>
status = eval(input())
status
status = eval(input())
23+j
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'j' is not defined
2+3j
(2+3j)
status = eval(input())
2+3j
status
(2+3j)
type(status)
<class 'complex'>
status = eval(input())
11.3
status
11.3
type(status)
<class 'float'>
status = eval(input())
'str'
status
'str'
status = eval(input())
100
status
100
status = eval(input())
1 2 3 4
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1
    1 2 3 4
      ^
SyntaxError: invalid syntax
status = eval(input())
[1,2,3,4]
status
[1, 2, 3, 4]
status = eval(input())
{1:1, 2:2, 3:3}
status
{1: 1, 2: 2, 3: 3}
status = eval(input())
(1,2,3,4)
status
(1, 2, 3, 4)
