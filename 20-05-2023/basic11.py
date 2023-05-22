'''
Write a Program to extract each digit from an integer in the reverse order.

For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
'''
input_number = 7536
#print(str(input_number)[3])
num_str = str(input_number) 
for item in num_str[::-1]:
    print(f"{item} ",end=" ")
