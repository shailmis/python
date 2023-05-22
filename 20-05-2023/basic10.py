'''
Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

Expected Output:

result list: [25, 35, 40, 60, 90]
'''
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
outList = []

for item in list1:
    if item%2 != 0:
        outList.append(item)

for item in list2:
    if item%2 == 0:
        outList.append(item)

print(f"{outList}")
