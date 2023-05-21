''' 
https://www.hackerrank.com/challenges/python-loops/problem

Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print i(square) , i^2
Example n = 3
The list of non-negative integers that are less than is [ 0 , 1, 2] . Print the square of each number on a separate line.
0
1
4
'''
n = int(input("Enter number n"))
for i in range(0,n):
    print (i*i)

        
