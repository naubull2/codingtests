import pdb


def binary_search(data, key, left, right):
    mid = (left + right) // 2
    while left <= right and left >= 0 and right < len(data):
        if data[mid] == key:
            return mid
        elif data[mid] > key:
            return binary_search(data, key, left, mid - 1)
        return binary_search(data, key, mid + 1, right)
    return None


print(binary_search([], 2, 0, 0))
