# coding: utf-8
import sys
import pytest
# Given two strings A and B, write a funciton can_shift to return whether or not A can be shifted some number of places to get B

"""
example)
A = 'abcde'
B = 'cdeab'

can_shift(A, B) == True
"""

def can_shift(a, b):
    # naive way to do this is to shift N (length of a) until we hit a == b
    # otherwise return False (no hits)
    if len(a) != len(b):
        return False
    i = 0
    while i < len(a):
        if a == b:
            return True
        a = a[1:] + a[:1]
        i += 1
    return False


    # may be check if a in b + b
    # [3,4,5,(1,2][3,4,5),1,2] will contain [1,2,3,4,5] at some point in the middle
    # take care of edges where 'aa', 'a' where simple repetition may occur
    if len(a)==len(b) and a in b+b:
        return True
    return False


    # MAY BE use KMP algorithm since there would be a great deal of overlap between A, B,
    # but KMP is not something you can think of in 15 mins unless memorized it




@pytest.mark.parametrize('a, b, result', [
    ('abcde', 'cdeab', True),
    ('abc', 'cba', False),
    ('aa', 'a', False),
    ('aab', 'baa', True)
])
def test(a, b, result):
    assert result == can_shift(a, b)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
