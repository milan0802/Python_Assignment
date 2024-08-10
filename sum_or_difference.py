"""Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5. """

x = int(input("Enter 1st value"))  
y = int(input("Enter 2nd value"))  

def function(x, y):
    if x == y or x+y == 5 or x-y == 5:
        print(True)  
#else:
    #print("False")
