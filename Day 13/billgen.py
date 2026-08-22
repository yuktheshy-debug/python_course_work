'''
data = {
    'sugar':50,
    'salt' :30,
    'cooking oil': 90,
    'eggs': 70,
    'peanuts':85,
    'rice':130,
    'butter':130,
    'bread':200,
    'wheatfloor':100
}

for i in data:
    print(i.ljust(20),data[i])

bill = 0
while True:
    product = input("Enter the product name or [E]xtra : ")
    if product == 'E' or product == 'e':
        print("Thanks for shopping")
        print("Total bil : ",bill)
        break
    else :
        quantity = int(input("Enter the quantity: "))
        bill += data[product]*quantity

            
a = input("enter products:").split()
print("----------Bill----------")
total = 0
for i in a:
    total = total + data[i]
    print(i.ljust(20),data[i])
print("------------------------")
print("Total bill:".ljust(20),total)'''



'''s = 'python programming'
d = {}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i] = 1
print(d)'''



'''s = 'aaaaaaasssssssddddddccctttaaaa'
c = 1
res = ''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c = c+1
    else:
        res = res + s[i] + str(c)
        c = 1
print(res+s[i]+str(c))'''