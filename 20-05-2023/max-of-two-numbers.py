'''
Given two numbers, write a Python code to find the Maximum of these two numbers.

Examples: 

    Input: a = 2, b = 4
    Output: 4

    Input: a = -1, b = -4
    Output: -1
'''
def max_of_two(num1,num2):
    if num1 > num2 :
        return num1
    else :
        return num2

print(f" Maximum of -1 and -4 is {max_of_two(-1,-4)}")
