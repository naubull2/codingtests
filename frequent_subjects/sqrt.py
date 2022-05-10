
def sqrt(x):
    if x == 1:
        return 1
    guess = x//2
    def _bsearch(val, left, right):
        sqr = val**2
        eps = 1e-7
        if sqr == x or abs(sqr-x) < 1e-2:
            return val
        if sqr < x:
            return _bsearch((val+right)/2, val+eps, right)
        else:
            return _bsearch((val+left)/2, left, val-eps)
    return int(_bsearch(guess, 0, x))

# iterative bsearch
def sqrt(x):
    left, right = 0, x
    while left < right:
        cnt += 1
        mid = (left + right) //2
        sqr = mid**2
        if sqr <= x and x < (mid+1)**2:
            return mid
        if sqr > x:
            right = mid
        else:
            left = mid
    return left

            
print(sqrt(5))
print(sqrt(3))
print(sqrt(9))
print(sqrt(8))
print(sqrt(4))
print(sqrt(36))
print(sqrt(2147395599))
print(sqrt(2147395600))


