"""Write a Python program to sum of three given integers. However, if 
two values are equal sum will be zero."""

x = int(input("Enter first value: "))
y = int(input("Enter second value: "))
z = int(input("Enter third value: "))

if x == y or y == z or z == x: 
    print("Sum:", 0)
else:
    plus = x + y + z  
    print("Sum:", 0)
