# coding: utf-8
# Copyright © 2022 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

	k == lists.length
	0 <= k <= 104
	0 <= lists[i].length <= 500
	-104 <= lists[i][j] <= 104
	lists[i] is sorted in ascending order.
	The sum of lists[i].length will not exceed 104.
"""
import pytest
from typing import Optional, List
from heapq import heapify, heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ans_head, curr_node = None, None
        # populate intial heap
        for i, h in enumerate(lists):
            if h:
                heappush(heap, (h.val, i))

        while heap: # O(N) as each node push/pop only once
            val, idx = heappop(heap) # our current smallest of k-lists O(logK)
            if curr_node is not None:
                curr_node.next = lists[idx]
            curr_node = lists[idx]
            if ans_head is None:  # need to point the very first for the output answer
                ans_head = curr_node

            lists[idx] = lists[idx].next
            if lists[idx] is not None:
                heappush(heap, (lists[idx].val, idx)) # O(logk)

        return ans_head


@pytest.mark.parametrize('', [
])
def test():
    pass

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
