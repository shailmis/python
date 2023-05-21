'''
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

    remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
    remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.

Note: n must be less than the length of the string.
'''
def remove_chars(in_string,pos):
    print(f"Inside function")
    for i in range(pos,len(in_string)):
        print(f"{in_string[i]}")

in_string = input("Enter Any string")
pos = int(input("Enter position"))
remove_chars(in_string,pos)
