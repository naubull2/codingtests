# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.

Constraints:

	1 <= changed.length <= 105
	0 <= changed[i] <= 105
"""
import pytest
from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, arr: List[int]) -> List[int]:
        # handle edges : odd size, zeros
        if len(arr) % 2:
            return []
        ans = []
        cnt = Counter(arr)
        if 0 in cnt:
            if cnt[0] % 2:
                return []
            else:
                ans.extend([0] * (cnt[0] // 2))
                cnt.pop(0)
                
        # don't sort the entire array, but only the keys (unique)
        for key in sorted(cnt.keys()):
            if not cnt:
                break
            if key in cnt:
                if 2 * key in cnt and cnt[key] <= cnt[2 * key]:
                    ans.extend([key] * cnt[key])
                    cnt[2 * key] -= cnt[key]
                    if cnt[2 * key] == 0:
                        cnt.pop(2 * key)
                    cnt.pop(key)
                else:
                    return []
        return ans


@pytest.mark.parametrize('arr, expected', [
    ([1,2,3,6], [1,3]),
    ([2,1,4,4,2,2], [1,2,2]),
    ([1,3,4,2,6,8], [1,3,4]),
    ([0], []),
    ([0, 0], [0])
])
def test(arr, expected):
    sorted(Solution().findOriginalArray(arr)) == expected

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
