# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

	The number of nodes in the list is in the range [1, 100].
	1 <= Node.val <= 100
"""
import pytest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def custom_list(l):
    # convert python list to a ListNode chain
    head = ListNode(val=l[-1])
    for e in l[:-1][::-1]:
        head = ListNode(val=e, next=head)
    return head


def pylist(h):
    # convert ListNode chain back to python list
    l = [h.val]
    while h.next:
        l.append(h.next.val)
        h = h.next
    return l


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _len = 1  # minimum size is 1
        iter_len = head
        while iter_len.next:
            iter_len = iter_len.next
            _len += 1
        _len //= 2
        while _len:
            head = head.next
            _len -= 1
        return head


@pytest.mark.parametrize(
    "node, expected", [([1, 2, 3, 4, 5], [3, 4, 5]), ([1, 2, 3, 4, 5, 6], [4, 5, 6])]
)
def test(node, expected):
    assert pylist(Solution().middleNode(custom_list(node))) == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
