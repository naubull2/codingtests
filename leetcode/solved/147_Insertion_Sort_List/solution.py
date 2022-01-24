# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

	Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
	At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
	It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Constraints:

	The number of nodes in the list is in the range [1, 5000].
	-5000 <= Node.val <= 5000
"""
import pytest
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    print(head.val)
    while head.next:
        head = head.next
        print(head.val)
        

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(head.val)
        def insert(prev, head, val):
            if head.val < val:
                if head.next:
                    insert(head, head.next, val)
                else:
                    head.next = ListNode(val)
            else:
                if prev:
                    node = ListNode(val, next=head)
                    prev.next = node
                else:
                    head = ListNode(val, next=head)
            return head

        while head.next:
            # move one node at a time
            head = head.next
            output = insert(None, output, head.val)
            
        return output
            

            


@pytest.mark.parametrize('arr, expected', [
    ([4,2,1,3], [1,2,3,4]),
    ([-1,5,3,5,0], [-1,0,3,4,5])
])
def test(arr, expected):
    assert Solution().insertionSortList(arr) == expected

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
