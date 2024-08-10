'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.'''

def swap_first_two_chars(s):
   
    if len(s) < 2:
        return s
  
    return s[1] + s[0] + s[2:]

def merge_and_swap(str1, str2):
    
    swapped_str1 = swap_first_two_chars(str1)
    swapped_str2 = swap_first_two_chars(str2)
    
    
    return swapped_str1 + ' ' + swapped_str2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = merge_and_swap(string1, string2)
print("Resulting string:", result)
