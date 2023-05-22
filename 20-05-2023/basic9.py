'''
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
'''
inStr = "542"
if inStr == inStr[::-1]:
    print("Palindrome")
    