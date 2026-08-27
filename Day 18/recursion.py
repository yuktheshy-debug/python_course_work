#function calling itself is called recursion
''' #syntax
def fun(arg):
    if base:
        return
    fun(up arg)
fun(par)
'''
'''
def display(n):
    if n==11:
        return
    print(n) #if n = 1 checks n = 11 else
    display(n+1) #add n+1 means 2 and 2+1 and 3+1.......10+1

display(1)

def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(10)
'''

def display(s,n): #s is the str and n is the index
    if n==len(s): #if index = length of s
        return
    print(s[n]) #if n = 0 then 0 is != len(s) so print s[0]
    display(s,n+1) 
display("Codegnan",0)