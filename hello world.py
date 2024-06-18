'''You are given a string containing words separated by spaces. Your task is to write a
function or program that reverses the order of words in the string.
Sample Input:
Hello World
Sample Output:
World Hello'''

def rev(inp):
    str=inp.split()
    rev=str[::-1]

    return ' '.join(rev)

inp_str=input("Enter a string: ")
rev_str=rev(inp_str)
print(rev_str)
