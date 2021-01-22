
import random

def binarySearch(nums, key):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right) // 2

        if key == nums[mid]:
            return mid
        elif key > nums[mid]:
            left = mid + 1
        else: 
            right = mid - 1

    return -1

nums = [10,20,30,40,50,60,70,80,90,100]

key = int(input("Enter value to search: "))

result = binarySearch(nums, key)

if result == -1:
    print("Value not found")
else:
    print("Found at", result+1)