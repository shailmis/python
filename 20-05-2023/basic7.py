'''
Write a program to find how many times substring “Emma” appears in the given string.
str_x = "Emma is good developer. Emma is a writer"
Output :- Emma appeared 2 times
'''

str_x = "Emma is good developer. Emma is a writer . Emma is a good orator too"
str_lst = str_x.split(' ')
substring = "Emma"
occur = 0
#print(f"{str_x.find(substring)}")
for x in str_lst:
    if x == substring:
        occur = occur + 1
print(f"{occur}")
