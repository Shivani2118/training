''' Peak Element Finder
Description: You are given an N- dimensional array arr[]. A peak element in the array 
is defined as an element whose value is greater than or equal to its neighboring 
elements (if they exist). Your task is to find the index of any peak element in the given 
array
Note: use 0-based indexing
Input:
An integer representing the number of elements in the array. N space-separated 
integers, denoting the elements of the array.
N space-separated integers ,denoting the elements of the array arr[]
Sample Input:
5
1 3 20 4 1
Sample Output:
2'''


def find_peak_element(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] >= arr[1]:
        return 0
    if arr[n-1] >= arr[n-2]:
        return n-1
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return i
arr = [1, 3, 20, 4, 1]
print(find_peak_element(arr))
