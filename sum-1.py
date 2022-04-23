#WAP to find total of numbers stored in List

numbers = [10,12,13,23,34,54]
total=0
#print(numbers)

for num in numbers:
    total = total+num
print ("the sum is ",total)

#WAP to find area of triangle

'''
formula
s=(a+b+c)/2
area=((s(s-a)*(s-b)*(s-c))**0.5
'''
a=float(input("Enter first side of triangle"))
b=float(input("Enter second side of triangle"))
c=float(input("Enter third side of triangle"))
s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)**0.5
print ("Area of triangle ",area)
