
def push(stack, data):
    stack.append(data)

def pop(stack):
    if stack == []:
        return "Underflow - Empty Stack"

    return stack.pop()

def display(stack):
    if stack == []:
        print("Underflow - Empty Stack")
        return

    for i in range(-1, -len(stack)-1, -1):
        print(stack[i])

    print()

stack = []

push(stack, 10)
push(stack, 20)
push(stack, 30)

display(stack)

print(pop(stack))
print(pop(stack))
print(pop(stack))
print(pop(stack))