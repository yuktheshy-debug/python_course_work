'''10..1

def display(n):

display(1)
'''
'''
def display(n):
    if n == 11: #untill n = 11
        return
    #before the recusrion it prints normal in a seq
    display(n+1) #after the recursion it will print in reverse
    print(n)

display(1)
'''
'''
def display(s, ind):
    if ind==len(s):
        return
    display(s, ind+1)
    print(s[ind], end=' ')

display("Codegnan", 0)'''

'''
def display(s,ind,w):
    if len(s)-w+1 == ind:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)

s = input("Enter the string : ")
w = int(input("Enter the width: "))
display(s,0,w)'''


'''
#iterate a list using recursion

def display(l,ind):
    if ind == len(l):
        return 0
    return l[ind] + display(l,ind+1)
l = [4,44,5,66,77]
print(display(l,0))'''

'''
#sum of digits using recursion

def display(n):
    if n == 0:
        return 0
    return (n % 10) + display(n // 10)  #gets the last digit and removes the last digit


n = 43567
print(display(n))
'''
'''
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
'''

'''
def fib(n):
    if n == 0 :
        return 0                   
    elif n == 1:
        return 1
    return fib(n-1)+fib(n-2) #here n = 5 means fib(5) = fib(4) + fib(3)
    for i in range(5):
    print(fib(i))
'''
'''
fib(0) = 0
fib(1) = 1
fib(2) = fib(1) + fib(0) = 1 + 0 = 1
fib(3) = fib(2) + fib(1) = 1 + 1 = 2
fib(4) = fib(3) + fib(2) = 2 + 1 = 3'''


'''   
n = int(input("Enter the num : "))
if n == 1:
    print(0)
elif n == 2:
    print(0,1)
else:
    a,b = 0,1
    print(a,b)
    for i in range(n-2):
        a,b = b,a+b
        print(b,end=' ')'''
