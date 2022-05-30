# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:

	1 <= nums.length <= 200
	1 <= nums[i] <= 100
"""
import pytest
from typing import List
from collections import Counter


## As a starter, we can approach with DP knapsack problem solution.
# class Solution:
#    def canPartition(self, nums: List[int]) -> bool:
#        # or we can approach as DP knapsack problem solution
#        s = sum(nums)
#        if s % 2 or len(nums) == 1:
#            return False
#
#        nums.sort(reverse=True)
#
#        @lru_cache(None)
#        def napsack(i, s):
#            if s == 0:
#                return True
#            if s < 0 or i == len(nums):
#                return False
#            # simply advance, or add nums[i] to the partition
#            return napsack(i+1, s - nums[i]) or napsack(i+1, s)
#
#        return napsack(0, s//2)


## An optimized solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (
            total % 2 or len(nums) == 1
        ):  # no odd sum can be partitioned in to two subsets
            return False

        cnt = Counter(nums)
        if all(cnt[k] % 2 == 0 for k in cnt):
            return True

        target = total / 2

        nums.sort(reverse=True)

        avg = total / len(nums)
        split = 0
        for i, n in enumerate(nums):
            if n <= avg:
                split = i
                break

        ## instead of searching entire space, we exchange elements between split at most N exchanges.
        def exchange(seta, setb, prior, target, count):
            print(f"target: {target} A:({sum(seta)}){seta}, B:{setb}")
            if not count:
                return False

            # shift nearest value to diff until target is met
            # always from B -> A
            diff = target - sum(seta)
            if diff == 0:
                return True

            shifted = False
            setb.sort(reverse=True)
            for i, e in enumerate(setb):
                if e <= diff:
                    # shift i
                    if e == prior:
                        i = i - 1
                    e = setb.pop(i)
                    seta.append(e)
                    prior = e
                    shifted = True
                    break
            if not shifted:
                ## See if any sufficient exchange(not shift) can be made
                for i, e1 in enumerate(setb):
                    for j, e2 in enumerate(seta):
                        if e1 > e2 and e1 - e2 == diff:
                            print(f"SWAP {e2}, {e1}")
                            return True

                # shift last
                if setb[-1] == prior:
                    e = setb.pop(-2)
                    seta.append(e)
                    prior = e
                else:
                    e = setb.pop(-1)
                    seta.append(e)
                    prior = e

            count -= 1
            if sum(seta) == target:
                return True
            else:
                # change shift direction if needed
                if sum(seta) < target:
                    return exchange(seta, setb, -1, target, count)
                return exchange(setb, seta, prior, target, count)

        return exchange(nums[split:], nums[:split], -1, target, 5 * len(nums))


@pytest.mark.parametrize(
    "nums, result",
    [
        ([2, 2, 3, 5], False),
        ([5, 3, 2, 2, 2, 2, 2, 2, 2], True),
        (
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                95,
                33,
            ],
            True,
        ),
        (
            [
                19,
                33,
                38,
                60,
                81,
                49,
                13,
                61,
                50,
                73,
                60,
                82,
                73,
                29,
                65,
                62,
                53,
                29,
                53,
                86,
                16,
                83,
                52,
                67,
                41,
                53,
                18,
                48,
                32,
                35,
                51,
                72,
                22,
                22,
                76,
                97,
                68,
                88,
                64,
                19,
                76,
                66,
                45,
                29,
                95,
                24,
                95,
                29,
                95,
                76,
                65,
                35,
                24,
                85,
                95,
                87,
                64,
                97,
                75,
                88,
                88,
                65,
                43,
                79,
                6,
                5,
                70,
                51,
                73,
                87,
                76,
                68,
                56,
                57,
                69,
                77,
                22,
                27,
                29,
                12,
                55,
                58,
                18,
                30,
                66,
                53,
                53,
                81,
                94,
                76,
                28,
                41,
                77,
                17,
                60,
                32,
                62,
                62,
                88,
                61,
            ],
            True,
        ),
        ([1, 2, 3, 5], False),
        ([3, 3, 3, 4, 5], True),
    ],
)
def test(nums, result):
    assert Solution().canPartition(nums) == result


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
