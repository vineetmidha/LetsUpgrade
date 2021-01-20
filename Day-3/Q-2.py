
'''
Q-2. Define a function swap that should swap two values and
print the swapped variables outside the
swap function.
'''

def swap():
    global a
    global b

    a, b = b, a
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Original values:")
print(f"a={a}, b={b}")

swap()

print("Swapped values:")
print(f"a={a}, b={b}")

'''
Output:

Enter first number: 10
Enter second number: 20
Original values:
a=10, b=20
Swapped values:
a=20, b=10
'''
