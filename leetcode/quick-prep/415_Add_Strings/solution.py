# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:

	1 <= num1.length, num2.length <= 104
	num1 and num2 consist of only digits.
	num1 and num2 don't have any leading zeros except for the zero itself.
"""
import pytest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """        
        carry = 0
        iterate strings num1, num2 from right to left,
            convert each digit, perform addition
            if take care of the carry

        any left over handling
        if any carry left
            add 1
        
        return final string- reversed
        """
        carry = 0
        i, j = len(num1)-1, len(num2)-1
        ans = []
        while i >= 0 and j >= 0:
            d1, d2 = int(num1[i]), int(num2[j])
            temp = d1 + d2 + carry
            carry, curr_digit = divmod(temp, 10)
            ans.append(str(curr_digit))
            i-=1
            j-=1
        
        while i >= 0:
            carry, digit = divmod(int(num1[i])+carry, 10)
            ans.append(str(digit))
            i-=1
        while j >= 0:
            carry, digit = divmod(int(num2[j])+carry, 10)
            ans.append(str(digit))
            j-=1
        
        if carry:
            ans.append('1')
        return ''.join(ans[::-1])
    


@pytest.mark.parametrize('n1, n2, result', [
    ('1', '99', '100'),
    ('456', '77', '533'),
    ('6994', '36', '7030')
])
def test(n1, n2, result):
    assert Solution().addStrings(n1, n2) == result

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
