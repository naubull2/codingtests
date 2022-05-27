

def merge_array(arr1, arr2, i, j, m, n):
    if m == 0:
        print('i is exhausted first')
        while n:
            arr1[i] = arr2[j]
            print(arr1)
            i += 1
            j += 1
            n -= 1
        return arr1
    elif n == 0:
        print('j is exhausted first')
        print(arr1)
        return arr1
    
    if arr1[i] < arr2[j]:
        #keep i
        print(f'keep i:{i}')
        print(arr1)
        return merge_array(arr1, arr2, i+1, j, m-1, n)
    else:
        arr1[i+1:] = arr1[i:-1]
        arr1[i] = arr2[j]
        print(f'insert j:{j} into i:{i}')
        print(arr1)
        return merge_array(arr1, arr2, i+1, j+1, m, n-1)

merge_array([1,2,3, 0, 0, 0], [2,5,6], 0, 0, 3, 3)
