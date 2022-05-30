# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

	The number of nodes in the list is in the range [1, 105].
	0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""
import pytest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Using two pointers we can scan the list, reverse a half along the way
        # time O(N), space O(1)
        if not head:
            return False
        slow_prev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow_prev, slow = slow_prev, slow, slow.next

        forward = slow.next if fast else slow
        backward = slow_prev
        while forward:
            if forward.val != backward.val:
                return False
            forward = forward.next
            backward = backward.next

        # But might want to restore the reversed chain.. in actual field
        return True


@pytest.mark.parametrize("", [])
def test():
    pass


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
