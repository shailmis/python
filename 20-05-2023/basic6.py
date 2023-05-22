'''
Iterate the given list of numbers and print only those numbers which are divisible by 5
'''
def divisible_by_five(in_lst):
    ret_list = []
    for i in range(len(in_lst)):
        if (in_lst[i]%5 == 0):
            ret_list.append(in_lst[i])
    return ret_list

in_lst = [10,23,43,44,5,15,55,20,50]
print(f"{divisible_by_five(in_lst)}")
