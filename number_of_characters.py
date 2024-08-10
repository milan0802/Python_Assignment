"""Write a Python program to count the number of characters (character
frequency) in a string """

str =input("Enter a string:")
chr={}
for n in str:
        if n in chr:
            chr[n] += 1
        else:
            chr[n] = 1
print("total characters:",chr)

