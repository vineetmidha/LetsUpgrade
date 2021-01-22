
import random


def selectionSort(mylist):
    for i in range(len(mylist)-1):
        min_index = i

        for j in range(i+1, len(mylist)):
            if mylist[j] < mylist[min_index]:
                min_index = j

        mylist[i], mylist[min_index] = mylist[min_index], mylist[i]

mylist = [random.randint(1,1000) for i in range(10)]

print("Original List:", mylist)

selectionSort(mylist)

print("Sorted List:", mylist)