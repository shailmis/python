'''
Write a program to accept a string from the user and display characters that are present at an even index number.
For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
'''

def print_even(in_str):
    for i in range(len(in_str)):
        if(i%2 == 0):
            print(f"{i} {in_str[i]}")
        

input_string = input("Enter String")
print_even(input_string)
