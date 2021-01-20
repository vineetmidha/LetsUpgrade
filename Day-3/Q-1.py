
'''
Q-1. Write a Python program to add two numbers using class and object.
(Take both numbers as input from the user)
'''

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def float_divide(self):
        return self.a / self.b

    def floor_divide(self):
        return self.a // self.b

    def display(self):
        print(f"a={self.a}, b={self.b}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

ob = calculator(a, b)

ob.display()

print("Sum:", ob.add())
print("Difference:", ob.sub())
print("Product:", ob.multiply())
print("Float Division:", ob.float_divide())
print("Floor Division:", ob.floor_divide())

'''
Enter first number: 10
Enter second number: 20
a=10, b=20
Sum: 30
Difference: -10
Product: 200
Float Division: 0.5
Floor Division: 0
'''
