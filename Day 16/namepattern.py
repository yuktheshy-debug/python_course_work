'''ABCDEFGHIJKLMNOPQRSTUVWXYZ


  0 1 2 3 4
0 * * * * *
1 *       *
2 *       *
3 *       *
4 * * * * *



n = int(input("Enter the size : "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 #if n is 5, 5//2 becomes 2 
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i == m:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i == m:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()


n = int(input("Enter the size : "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
            print('*', end=' ')
        else:
            print(' ',end = ' ')
    print()

n = int(input("Enter the size : "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j==n-1 or i==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))

m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1  or i+j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or i+j == n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == m :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or (i==j and i>=m) or (i+j == n-1 and i<=m) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if i == 0 or i ==n-1 or (i==j and j<=m) or (i+j == n-1 and j<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i==j and i>=m) or (i+j == n-1 and i>=m) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i==m :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j==m :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j==m and i+j==m+n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i==n-1 or j==n-1 or i+j==m+n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the size : "))
m = n//2 
for i in range(n):
    for j in range(n):
        if j == i or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


