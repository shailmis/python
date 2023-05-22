'''
Write a function to return True if the first and last number of a given list is same. 
If numbers are different then return False.
Given list: [10, 20, 30, 40, 10]
result is True
'''
def first_last_same(in_lst):
    #print(f"{in_lst}")
    if in_lst[0] == in_lst[-1]:
        return True
    else:
        return False

in_lst = [10,23,32,33,45,34,10]
print(f"{first_last_same(in_lst)}")
