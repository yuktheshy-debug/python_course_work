'''import sys

print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
sys.exit()
print("end")


import platform

print(platform.system())
print(platform.release())
print(platform.processor())
'''
'''
import math

print(math.pi)
print(math.e)

print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(8,12))
print(math.sqrt(36)) #gives op as float
print(math.pow(2,3)) #gives op as float


print(round(12.0000000001))
print(round(12.3))
print(round(12.6666))
print(round(12.9999999))


print(math.ceil(12.0000000001))
print(math.ceil(12.3))
print(math.ceil(12.6666))
print(math.ceil(12.9999999)) #ceil gives above like even though 12.9999 gives 13


print(math.floor(12.0000000001)) 
print(math.floor(12.3))
print(math.floor(12.6666))
print(math.floor(12.9999999)) #here it gives 12
'''
'''
import random

random.seed(9)

print(random.random()) #gives result bw 0-1 in float
print(random.randint(1000000,999999999)) #gives nbr bw 1-6
print(random.uniform(1,6)) #gives random value bw 1-6 in float

l = ['r','p','s']
print(random.choice(l))

lang = ['python','java','css','javascript','flask']
print(random.choices(lang,k=2)) #gives or picks any two 

random.shuffle(lang)
print(lang) #shuffles all 
'''
'''
s = 'python programming'
d = {}

for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)
'''

'''
from collections import Counter

s = 'python programming'
res = Counter(s)
print(res)
'''


'''
from collections import Counter,defaultdict

products = ['sugar','salt','milk']
res = defaultdict(list)

for i in products:
    res[i].append(['des','rev','com'])

print(res)
'''
from collections import Counter,defaultdict,deque

l = deque([ ])

l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.append(50)
l.append(60)
l.popleft()

print(l)

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop() 
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()

print(l)