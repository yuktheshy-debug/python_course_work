#syntax for lambda
'''
var = lambda arg : exp


wish = lambda name : f"Welcome to the course {name}"
print(wish("Yuk"))
print(wish("Yukthesh"))

gst = lambda price : price+price*0.18
print(gst(1000))
print(gst(2000))

avg = lambda a,b,c : (a+b+c) / 3
print(avg(24,34,56))
print(avg(78,25,56))

iseven = lambda a :  "Even" if a%2==0 else "Odd"
print(iseven(16))
print(iseven(190))

largest = lambda a,b,c : a if a>b and a>c else ( b if b > c else c)
print(largest(22,33,44))
print(largest(22,57,74))

isvowel = lambda a :  "Vowel" if a in 'aeiouAEIOU' else "Cons"
print(isvowel('u'))
print(isvowel('g'))


l = [1,2,3,4,5,6,7]
update = list(map(lambda i : i+10,l)) #map is used to upd each elem
print(update)


t = (787,567,897,465)
discount = list(map(lambda i : i-i*0.3,t))
print(discount)


l = [1,2,3,4,5,6,7]
update = list(filter(lambda i : i%2!=0,l)) #filter will display the elem if they satisfy the given condition
print(update)


t = (787,5967,897,67465)
discount = list(filter(lambda i : i>1000,t))
print(discount)


l = ['yukthesh@codegnan.com','yukthesh@yahoo.com','yukthesh@gmail.com','yukthesh@snapchat.com']

res = list(map(lambda i : i.split('@')[-1],l))
print(res)
#whenever you need to update each value use map, based on codn use filter


from functools import reduce

l = [4,2,4,64,75,2,4645,8]

res = reduce(lambda sum,i: sum+i,l)  #reduce by adding all the values (combine all values)
print(res)

l = [4,2,4,64,75,2,4645,8]
res1 = reduce(lambda sum,i: sum * i,l)  #reduce by multiplying each value
print(res1)
'''
'''
res1 = reduce(lambda pro,i:pro*i,l)
print(res1)
'''
'''
seats = {'s1':True,
         's2':False,
         's3':False,
         's4':False,
         's5':True,
         's6':True}
aval = list(filter(lambda i : seats[i]!=True,seats))
print(aval)

products = {
    'eggs':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}

res = list(filter(lambda i: products[i]>50,products))
print(res)
'''

#from low to high
products = {
    'eggs':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}

print(dict(sorted(products.items(),key = lambda i:i[1])))
print(dict(sorted(products.items(),key = lambda i:i[1],reverse = True)))
