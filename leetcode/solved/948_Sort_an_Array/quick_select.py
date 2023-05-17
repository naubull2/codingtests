def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def quickselect(arr, l, r, k):
    if (k > 0 and k <= r-l+1):
        index = partition(arr, l, r)
        if (index-l == k -1):
            return arr[index]

        if (index-l > k-1):
            return quickselect(arr, l, index-1, k)
        return quickselect(arr, index+1, r, k-index+l-1)
    raise IndexError("k is out of bound for arr")


arr = [2, 2, 2, 2, 2, 2, 2, 2]
n = len(arr)
k = 4

print(quickselect(arr, 0, n-1, k))
