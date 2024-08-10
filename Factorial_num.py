# Write a Python program to get the Factorial number of given number.

n = int(input("Enter the number: "))
fact = 1

print("Factorial of is ")
for i in range(1, n+1):
    fact = fact * i
print(fact)

