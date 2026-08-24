'''for i in range(5):
    for j in range(3):
        print(j,end= ' ')
       #outer row is called as i (horizontal) / rows
            #inner row is called as j (vertical) / columns

for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()

for i in range(5):
    for j in range(5):
        print(j%2,end=' ') #values are changing by columns so 'j'
    print()

for i in range(5):
    for j in range(5):
        print(i%2,end=' ') #values are changing by rows so 'i'
    print()

for i in range(5):
    for j in range(5):
        print((i+j)%2,end='') #to check the sum of i and j is even or odd
    print()

for i in range(5):
    for j in range(5):
        print((i+j),end=' ')
    print()
c = 1
for i in range(5):
    for j in range(5):
        print(c,end=' ') #if there is no relation bw i and j use another var from outside
        c+=1
    print()

for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print()
n = 5
for i in range(5):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

n = 5
for i in range(n):
    for sp in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()

n = 9
m = n//2
for i in range(n):
    if i <= m:
        for j in range(i+1):
            print('*',end=' ')
    else :
        for k in range(n-i):
            print('*',end=' ')
    print()

#lets optimize this one

n = 9
m = n//2
for i in range(n):
    if i <= m:
        print('*'*(i+1),end=' ')
    else :
        print('*'*(n-i),end=' ')
    print()

n = 9
m = n//2
for i in range(n):
    if i <= m:
        print(' '*(m-i),'*'*(i+1),end=' ',sep=' ')
    else:
        print(' '*(i-m),'*'*(n-i),end=' ',sep=' ')
    print()'''