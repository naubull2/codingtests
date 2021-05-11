# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

Constraints:

	3 <= arr.length <= 3000
	0 <= arr[i] <= 100
	0 <= target <= 300
"""
import pytest

from collections import Counter

class Solution(object):
    def threeSumMulti(self, A, target):
        num_counter = Counter(A)
        sorted_values = sorted(list(num_counter.keys()))
        ans = 0
        edge = max(A)
        # x == y == z
        if target % 3 == 0:
            x = target // 3
            if 0 <= x <= edge:
                ans += num_counter[x] * (num_counter[x] - 1) * (num_counter[x] - 2) // 6

        for i, x in enumerate(sorted_values):
            # x < y < z
            for y in sorted_values[i+1:]:
                z = target - x - y
                if y < z <= edge:
                    ans += num_counter[x] * num_counter[y] * num_counter[z]
            # x == y
            z = target - 2*x
            if x < z <= edge:
                ans += num_counter[x] * (num_counter[x] - 1) // 2 * num_counter[z]

            # y == z
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if x < y <= edge:
                    ans += num_counter[x] * num_counter[y] * (num_counter[y] - 1) // 2
                    
        return ans % (10**9 + 7)

@pytest.mark.parametrize('arr, target, expected', [
    ([1,1,2,2,3,3,4,4,5,5], 8, 20),
	([1,1,2,2,2,2], 5, 12)
])
def test(arr, target, expected):
	assert Solution().threeSumMulti(arr, target) == expected

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
