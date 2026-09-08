#looping statements used for repeating statements

#str list tuple set dict range
'''
for var in seq:
    #stmts'''

'''s = 'python programming'
for i in s:
    print(i)'''

'''num= [1,2,3,4,5]
for i in num:
    print(num)'''

'''prices = (987,234,567)
for price in prices:
    print(prices)'''

'''names = {'mounasri','lohitha','usharani'}
for name in names:
    print(names)'''

'''d = {1:1,2:2,3:3}
for i in d:
    print(i)'''

#range is used for generating numeric value

#range(start,end+1,step):(0,,1)
'''for i in range(1,11):
    print(i)'''

'''for  i in range (2,21,2):
    print(i)'''

'''for i in range(5,101,5):
    print(i)'''

'''for i in range(5,10,-1):
    print(i)'''

#for index value use range fumctiom
'''s = 'Java programming'
for i in range(len(s)):
    print(i,s[i])

s = 'python programming'
for i in range(len(s)):
    print(i,s[i])

#only for indexing 
s = (456,234,123)
for i in range(len(s)):
    print(i,s[i])'''


#enumerate id gng to give us the seq
'''s = [6789,3455,7889]
for i in enumerate(s):
    print(i[0],i[1])'''

'''d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])#to access keys and values'''

'''for i in range(1,11):
    if i==5:
        break#terminates means it stops there
    print(i)

for i in range(1,11):
    if i==5:
        continue #continues by skipping that mentioned ele
    print(i)

for i in range(1,11):
    if i==51:
        break
    print(i)
else :
    print("End of the loop")

l = [12,13,14,15,16,17]
n = 26
for i in l:
    if i == n:
        print(n,"found")
    else :
        print(n,"Not found")

pin = 1234
for i in range(5):
    epin = int(input("Enter the pin : "))
    if epin == pin:
        print("Unlock phone")
        break
    else :
        print("invalid pin")
else : 
    print("Try after 30 seconds")

password = 'yukthesh'
for i in range(5):
    epass = (input("Enter the password : "))
    if epass == password:
        print("Unlock phone")
        break
    else :
        print("invalid password")
else : 
    print("Try after 30 seconds")


#to check whether it is prime number
n = 14
for i in range(2,n//2+1): 
    if n%i==0:
        print(n,"Not a prime number")
        break
    else : 
        print(n,"Prime number")'''

n = 34
for i in range(2,n//2+1):
        if n%i==0:
            print(n,"Not a prime number")
            break
        else :
            print(n,"is prime number")

