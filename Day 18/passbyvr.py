#int float complex str list tuple dict set bool

#only list set dict are "pass by var" (effects the outside fn) mutable
#remaining all are pass by values (which are immutable) wont effect the outside fn

'''
def display(n):
    n += 10
    print("Inside the function : ",n)

n = 10
display(n)
print("Outside the function",n)


def display(n):
    n += 10.3
    print("Inside the function : ",n)

n = 10
display(n)
print("Outside the function",n)


def display(n):
    n += 10+3j
    print("Inside the function : ",n)

n = 10
display(n)
print("Outside the function",n)


def display(n):
    n += "lang"
    print("Inside the function : ",n)

n = "python"
display(n)
print("Outside the function",n)


def display(n):
    n.append(5)
    print("Inside the function : ",n)

n = [1,2,3,4]
display(n)
print("Outside the function",n)


def display(n):
    n.add(5)
    print("Inside the function : ",n)

n = {1,2,3,4}
display(n)
print("Outside the function",n)
'''

'''
def display(n):
    n[5]=6
    print("Inside the function : ",n)

n = {1:2,3:4}
display(n)
print("Outside the function",n)


def display(n):
    n += (4,5,6)
    print("Inside the function : ",n)

n = (1,2,3,4)
display(n)
print("Outside the function",n)''' 