'''def functionname(arg):
    #stmnts
    return (opt)

functionname(parm)'''

'''def gst(price):
    print("Original price : ", price)
    print("Final price :", price+price*0.18)

gst(1000)
gst(7800)
gst(500)
gst(800)
gst(10000)'''

'''def table(n):
    print(f"{n} Table")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

table(9) #you need to call the function

def table(n):
    print(f"{n} Table")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

for i in range(1,21):
    table(i)''' #once we written the logic no need to write it again

#to check whether it is leap year or not
'''def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap year"
    else:
        return "Not a leap year"

print(isleap(2012))
print(isleap(2015))
print(isleap(2026))'''

'''def isprime(num):
    for i in range(2,num//2+1):
     if num%i==0:
        return "Not a Prime number"
    else:
        return "Prime number"

print(isprime(5))
print(isprime(6))
print(isprime(9))
print(isprime(4))'''

#Types of arguments
#POSITIONAL ARGUMENT

'''def display(name,email,pwd):
    print("name :", name)
    print("email :", email)
    print("pwd :", pwd)

display('Yukthesh','yuktheshy@gmail.com','yukthesh123')
display('Yukthesh@gmail','yukthesh','yukthesh123')
display('Yukthesh123','yukthesh','yuktheshy@gmail.com')

#based on the positions it gives the output'''
'''
#KEY WORD ARGUMENT
#depends on the keys 
#the mapping is based on the keys

def display(name,email,pwd):
    print("name :", name)
    print("email :", email)
    print("pwd :", pwd)

display(name='Yukthesh',email='yuktheshy@gmail.com',pwd='yukthesh123')
display(email='Yukthesh@gmail',name='yukthesh',pwd='yukthesh123')
display(pwd='Yukthesh123',name='yukthesh',email='yuktheshy@gmail.com')

#gives op based on keys in this argument
'''
'''#DEFAULT ARGUMENT
#if user didnt send a name just replace it with a noun
#if user didnt send a num just replace it with a int

def display(name,email,pwd= None):
    print("name :",name)
    print("email :",email)
    print("pwd :",pwd)

display("yukthesh","email")
display("yukthesh","email","pwd@gmail")'''
'''
#VARIABLE NAME ARGUMENT
def display(*names):
    print(names)

display("yukthesh")
display("yukthesh","yuk")
display("yukthesh","yuk","ssr")
display("Yukthesh","yuk","ssr","yu")#displays as tuple
'''
#whenever we have keys and values we need to use double **
def display(**names):
    print(names)

display(n1="yukthesh")
display(n1="yukthesh",n2="yuk")
#then it displays as dictionaries(key value pairs)