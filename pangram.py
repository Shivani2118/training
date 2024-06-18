'''Pangram is a sentence containing every letter in the English alphabet. Given a string, 
find all characters that are missing from the string, Le., the characters that can make 
the string a Pangram We need to print output in alphabetic order.
For example,
Input: welcome to geeksforgeeks
Output: abdhijnpquvxyz'''

def pangram(input_string):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    input_string = input_string.lower()
    
    missing_chars = []
    
    for i in alphabet:
        if i not in input_string:
            missing_chars.append(i)
    
    missing_chars.sort()
    print(''.join(missing_chars))

input_string = input("Enter a string: ")
pangram(input_string)
