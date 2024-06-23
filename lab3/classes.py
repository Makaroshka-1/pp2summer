import math

class RandomClass:
    def __init__(self):
        self.text = input()
    def getString(self):
        return self.text
    def printString(self):
        print(self.text.upper())

class Shape:
    def __init__(self):
        self.area = 0
    def area(self):
        return self.area
    
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length*self.length
    
class Reactangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

class Points:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    def show(self):
        return Points()
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.x)**2)

class Account:

    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,value):
        self.balance += value
        return self.balance

    def withdraw(self,value):

        if value > self.balance:
            return "Not enough funds "
        
        self.balance-=value
        return self.balance                

# filter functions here 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n//0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1,23,4,5,516,54,5,1,41,62,5,1,23,1,14,14,51,1 ]
prime_numbers =  list(filter(lambda x:is_prime(x), numbers))

square = Square(50)
print(square.area())

rect = Reactangle(12,50)
print(rect.area())