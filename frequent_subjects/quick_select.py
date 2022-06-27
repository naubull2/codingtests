# coding: utf-8
import sys
import pytest

# Given a array of integers, find the k-th smallest element in O(n)

"""
example)
arr = [7, 10, 4, 3, 20, 15]
k = 4

output = 10
"""

def quick_select(arr, k):
    return select_at(arr, 0, len(arr)-1, k) 

def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        # for l to r-1, compare with pivot
        if arr[j] <= pivot:
            # swapping in anything less than pivot from left to right(stable sort)
            arr[i], arr[j] = arr[j], arr[i]  
            i+=1
    # insert pivot to the place (i)
    arr[i], arr[r] = arr[r], arr[i] 
    return i
        

def select_at(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot_idx = partition(arr, left, right)
    if k-1 == pivot_idx:
        return arr[k]
    elif (k-1) < pivot_idx:
        right = pivot_idx-1
    else:
        left = pivot_idx+1
    return select_at(arr, left, right, k)


@pytest.mark.parametrize('arr, k, output', [
    ([7, 10, 4, 3, 20, 15], 4, 10)
])
def test(arr, k, output):
    assert output == quick_select(arr, k)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
