# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1

Constraints:

	1 <= bad <= n <= 231 - 1
"""
import pytest


# The isBadVersion API is already defined for you.
def isBadVersion(version: int, bad: int) -> bool:
    if version == bad:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int, bad: int) -> int:
        # Binary search into the array of list(range(n))
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            isbad = isBadVersion(mid, bad)
            if isbad:
                if isBadVersion(max(1, mid - 1), bad):
                    # search left half
                    high = mid - 1
                else:
                    # it's bad and it's first
                    return mid
            else:
                low = mid + 1
        return low


@pytest.mark.parametrize("n, bad", [(5, 4), (1, 1)])
def test(n, bad):
    assert Solution().firstBadVersion(n, bad) == bad


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
