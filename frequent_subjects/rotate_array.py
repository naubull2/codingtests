"""
Rotate an array of N elements to the right by k steps

For example with n=7, k=3, 
 array = [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]

 How many different ways to solve this?
"""

# 1. Intermediate array
# Using extra space for the output array, we simply copy elements over from k+
# If not using pythonic string slicer,

def shift(arr, k):
    ans = []
    count = size = len(arr)
    i = size - k
    while count > 0:
        ans.append(arr[i])
        i = (i+1) % size
        count -= 1
    return ans

''' In more pythonic way of doing it in-memory
def shift(arr, k):
    arr[:] = arr[-k:] + arr[:-k]
    return arr
'''


# 2. bubble rotate
# bring last k values to the front of the array by bubbling (swapping)
# space O(1) for temp value to swap across
# time O(N*k)

def shift(arr, k):
    for i in range(k):
        # perform bubbling k times
        for j in range(len(arr)-1, 0, -1):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
    return arr


# 3. reverse arrays
# O(N) time, O(1) space
# but this is quite inefficient way of O(N) as the multiple is quite large
# T(cN)
def shfit(arr, k):
    def reverse(l):
        for i in range(len(l)//2):
            t = l[i]
            l[i] = l[-i]
            l[-i] = t

    reverse(arr)
    reverse(arr[k:])
    reverse(arr[:k])
    return arr


array = list(range(1, 8))
print(array)
print(shift(array, 3))

