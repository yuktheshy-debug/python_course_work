#while loop
#to print 1 to 10 nbrs
'''i = 1        #intialize
while i<=10:    #base
    print(i)    #updation
    i+=1

#from 10 to 1

i = 10
while i > 0:
    print(i)
    i-=1

#multiples of 5
i = 5
while i<=50:
    print(i)
    i+=5

#string

s = 'while loop'
i = len(s)-1
while i>=0:
    print(s[i])
    i-=1


l = [3456,5678,5678]#display list using while
i = 0
while i<len(l):
    print(l[i])
    i+=1

n = 8765
while n>0:
    print(n%10) #reminder
    n//=10

n = 9876589098
sumofdigits = 0
while n>0:
    sumofdigits += n%10
    n//=10
print("Sum of digits :",sumofdigits)

n = 9876589098
proofdigits = 1
while n>0:
    proofdigits *= n%10
    n//=10
print("Sum of digits :",proofdigits)

n = 34567
res = 0
while n > 0 :
    rem = n%10
    res = res*10 + rem
    n//=10

print(res)

n = 87654
res = 0
while n > 0:
    rem = n%10
    if rem%2==0:
        res += rem
    n//=10

print(res)

l = [7,9,23,0,0,0,12,0,13,1,0,1,5,6,7,8,0]
while 0 in l:
    l.remove(0)
print(l)'''

l = [2,3,6,76,12,4,5,61,4,5,2,23]
i,j = 0,len(l)-1
while i <= j:
    if i==j:
        print(l[i])
    else :
        print(l[i]+l[j])
    i+=1
    j+=-1