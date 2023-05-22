'''
Print downward Half-Pyramid Pattern with Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*

'''
rows = 5
for row in range(rows):
    for col in range(row):
        print(f"*" , end=" ")
    print("\n")
