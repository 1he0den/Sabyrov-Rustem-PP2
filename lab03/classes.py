

## 1

class ConsoleString:

    def __init__(self):
        self.string = ''
        
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

console_string = ConsoleString()
console_string.getString()  
console_string.printString()


## 2

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
square = Square(5)


## 3

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


shape = Shape()
rectangle = Rectangle(4, 6)

## 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Координаты точки: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()  
point1.move(4, 5)
point1.show()  
print("Расстояние между точками:", point1.dist(point2))  


## 5

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} успешно зачислено. Текущий баланс: {self.balance}")
        else:
            print("Сумма для зачисления должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете.")
        elif amount <= 0:
            print("Сумма для снятия должна быть положительной.")
        else:
            self.balance -= amount
            print(f"{amount} успешно снято. Текущий баланс: {self.balance}")

account = Account("Jake", 1000)
account.deposit(500)     
account.withdraw(200)    
account.withdraw(2000)   
account.deposit(-100)    


## 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Простые числа в списке:", prime_numbers)