#local variable
#global variable
'''
#local variable
def display():
    n = 10
    print("Inside function :",n) #which can only access the value inside 

display()
print("Outside function :",n)

#global variable
def display():
    print("Inside function :",n)

n = 10
display()
print("Outside function",n) #which can access the values in both inside and outside (globally)


#to access the inside vairable globally
def display():
    global n   #to access the inside one globally we need to use this fn
    n = 10
    print("Inside function: ",n)

display()
print("Outside function",n)


def display():
    global n
    n += 10 #if we add changes inside it also effects the outside var
    print("Inside function :",n)

n = 10
display()
print("Outsdie function",n)

#and no need to give parameters inside because it atomatically takes the values


def display():
    course = "PFS"
    def update():
        nonlocal course #makes the both in and out 
        course = 'JFS'
        print("Inner function",course)
    update()
    print("Outer function",course)

display()
'''

s = [1,2,3,4,5]
print(sum(s))

sum = 20
print(sum)  #here no need to write sum(l) if we write like this it acts as a var so it shows error let it be function only 