
def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if queue == []:
        return "Underflow - Empty Queue"

    return queue.pop(0)

def display(queue):
    if queue == []:
        print("Underflow - Empty Queue")
        return

    for i in queue:
        print(i, " => ", sep="", end="")

    print()

queue = []

enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)
enqueue(queue, 40)

display(queue)

print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))