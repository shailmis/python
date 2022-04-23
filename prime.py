#Program to check if given number is prime

#number=155

number=int(input("Enter number"))

if number > 1:
    #check for factors
    for i in range(2,number):
        if (number%i) == 0 :
            print ( number, " is not prime" )
            print ( i, "times " ,number//i,"is",number) 
            break
    # This else is of for loop which means that all range values are exhausted
    else:
            print (number, "is a prime" )

#This else is if number is less than 1 or negative
else:
    print (number,"is not prime")
        
        
    



