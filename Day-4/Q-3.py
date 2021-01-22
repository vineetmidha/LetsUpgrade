
# Q-3: Write a Python program to find the middle of a linked list.

class Node:

    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        new = Node(data)
        
        if self.head == None:
            self.head = new
        else:

            current = self.head

            while current.next != None:
                current = current.next

            current.next = new

    def middleNode(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        print("Middle Node:", slow.data)

    def display(self):
        current = self.head

        while current != None:
            print(current.data, end="=>")
            current = current.next

        print()

mylist = LinkedList()

mylist.insertEnd(10)
mylist.insertEnd(20)
mylist.insertEnd(30)
mylist.insertEnd(40)
mylist.insertEnd(50)

mylist.display()

mylist.middleNode()

