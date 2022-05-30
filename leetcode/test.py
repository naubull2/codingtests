import sys
import pdb


def count_primes(n):
    isPrime = [False] * 2 + [True] * (n - 2)
    i = 2
    while i * i < n:
        if not isPrime[i]:
            i += 1
            continue
        j = i * i
        while j < n:
            isPrime[j] = False
            j += i
        i += 1
    print(isPrime)
    return isPrime.count(True)


count_primes(10)
