# Question 1

# Implement deletion operation from the end of the linked list and 
# Insertion operation from the beginning of the linked list


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

    def deleteEnd(self):
        current = self.head
        prev = self.head

        while current.next != None:
            prev = current
            current = current.next

        prev.next = None

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

mylist.deleteEnd()

mylist.display()
