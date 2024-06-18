'''8) Smallest Number
Prince participated in three Olympiads at school and received marks for all of them. 
He is interested in finding out the lowest mark he obtained among the three 
Olympiads. Write a program to find the minimum mark.
Example:
Input: 50 66 23
Output: Smallest number is 23'''

def smallest(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<b and c<a:
        return c
n1=int(input())
n2=int(input())  
n3=int(input())
print(smallest(n1,n2,n3))
