#operators are only used to deal with variables 
#but not for obj but here we use magical methods to apply 

class Numbers:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __floordiv__(self,other):
        return self.n // other.n
    def __mod__(self,other):
        return self.n % other.n
    def __pow__(self,other):
        return self.n ** other.n
    def __gt__(self,other):
        return self.n > other.n
    def __lt__(self,other):
        return self.n > other.n
    def __ge__(self,other):
        return self.n >= other.n
    def __le__(self,other):
        return self.n <= other.n
    def __eq__(self,other):
        return self.n == other.n
    def __ne__(self,other):
        return self.n != other.n
    def __str__(self):
        return str(self.n)


a = Numbers(10)
b = Numbers(2)


print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

