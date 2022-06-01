# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

	"AAJF" with the grouping (1 1 10 6)
	"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:

	1 <= s.length <= 100
	s contains only digits and may contain leading zero(s).
"""
import pytest


class Solution:
    def numDecodings(self, s: str) -> int:
        # read in letters as long as it fits under [1, 26]
        # then for break points we can recurse into the cases
        # for the same remainder, we can use memoization to boost up
        # -> Dynamic programming approach
        '''
        Recurrence relation would be like
        
        for some position at i in string s,
        
        possible prefixes include
          i, i+1, (we can't have three digit number since the range is 1-26)
          DFS(i) = DFS(i+1) + DFS(i+2)
          
          
        # we can build bottom up DP, we don't need entire table to fill, but
        # just two variables to build
        # ways[i] = ways[i+1] + ways[i+2]
        
        '''
        # 1. DP bottom up
        # we can further save DP memory as we don't need the entire DP table
        dp1, dp2 = 1, None 
        # return possible number of parsing starting from i
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
            
            if (i+1 < len(s) and (s[i] == "1" or
              (s[i] == "2" and s[i+1] in "0123456"))
            ):
                dp += dp2
            dp1, dp2 = dp, dp1
        return dp
        
        # 2. DP recursion
        """
        Try "123"
        res  2 
              2
               1
            2 +1= 3
        1, 2, 3
        12, 3
        1, 23
        """
        dp = {len(s): 1}
        def parse(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = parse(i+1)
            if (i + 1 < len(s) and (s[i] == "1" or 
              s[i] == "2" and s[i+1] in "0123456")
            ): # double digit is valid
                res += parse(i+2)
            dp[i] = res
            return res
        
        return parse(0)
        

@pytest.mark.parametrize('s, num', [
    ("12", 2),
    ("123", 3)
])
def test(s, num):
    assert Solution().numDecodings(s) == num

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
