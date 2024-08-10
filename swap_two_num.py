#Write python program that swap two number with temp variable and without temp variable.

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print("***************************")
print("Before swapping:")
print("x :", x)
print("y :", y)
x = x + y
y = x - y
x = x - y
print("***************************")
print("After swapping:")
print("x :", x)
print("y :", y)



