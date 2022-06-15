# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:

	-100.0 < x < 100.0
	-231 <= n <= 231-1
	-104 <= xn <= 104
"""
import pytest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        !!! Take care of negative ns

        x^n = x^(a+b) = x^a * x^b
        
        we are essentially looking for n's additive splits?
         - where series of a,bs add up to total of n.
        
        In binary,
        n
        5 = 101(2) = 2^2 + 2^0
        8 = 1000(2) = 2^3
               base   output
        5 odd   x     1*x
        2 even  xx    -
        1 odd   xxxx  x * xxxxx => we have 5 xs
        """
        if n < 0:
            x = 1/x
            n = -n

        base = x
        ans = 1
        while n > 0: 
            if n % 2 == 1:
                ans *= base
            base *= base
            n//=2
        return ans

        # OR just write a recursion
        #def split(base, power):
        #    if not power: return 1
        #    #x^power//2 * x^power//2
        #    half = split(base, power//2)
        #    if power % 2:
        #        return half*half*base
        #    return half * half
        #return split(x, n)
        
            

@pytest.mark.parametrize('x, n, result', [
    (2., 10, 1024.),
    (2.1, 3, 9.261),
    (2., -2, 0.250)
])
def test(x, n, result):
    assert round(Solution().myPow(x, n), 3) == round(result, 3)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
