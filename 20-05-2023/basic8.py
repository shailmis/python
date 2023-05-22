'''
Print following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

first row, 1 char ( 1 one times)
second row, row value row times ( 2, 2 times)
third row, row value row times ( 3 , 3 times)
Hint 
1) print next line outside nested loop
2) print row value inside nested loop
3) inside loop should run row times

'''
rows = 6
col = 0
for row in range(1,rows):
    for printChar in range(row):
        print(f"{row}", end=" ")
    print("\n")
    
    
