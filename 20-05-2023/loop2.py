'''
Given a list, write a Python program to swap first and last element of the list.
Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
'''
input_list = [12,35,9,56,24]
input_list[0] , input_list[-1]= input_list[-1] , input_list[0]
print(input_list)
