'''
1) Signature for LCM
Given two numbers a and b. Find the GCD and LCM of and d.
Input:
• Two positive integers a and b (1 <=a, b <=1000)
Output:
For GCD function, an integer representing the GCD of a 'and b
For LCM function, an integer representing the LCM of a and b
Sample Input:
12 18
Output:
6
36

'''
def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
def compute_lcm(x, y):
    gcd = compute_gcd(x, y)
    return abs(x * y) // gcd
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd = compute_gcd(num1, num2)
print("The G.C.D. is", gcd)
lcm = compute_lcm(num1, num2)
print("The L.C.M. is", lcm)
