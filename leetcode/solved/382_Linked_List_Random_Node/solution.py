# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

	Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
	int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

Example 1:

Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.

Constraints:

	The number of nodes in the linked list will be in the range [1, 104].
	-104 <= Node.val <= 104
	At most 104 calls will be made to getRandom.

Follow up:

	What if the linked list is extremely large and its length is unknown to you?
	Could you solve this efficiently without using extra space?
"""
import pytest


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # it's either O(N) for space or runtime trade offs.
    # If getRandom is to be called often, we use space to boost runtime,
    # If not, then we should use reservoir sampling to O(N) getRandom, saving space complexity to O(1)

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        self.arr.append(head.val)
        while head.next:
            head = head.next
            self.arr.append(head.val)
        self.n = len(self.arr)

    def getRandom(self) -> int:
        cnt = random.randrange(0, self.n)
        return self.arr[cnt]


class Solution:
    # NOTE: reservoir sampling to save space
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        pt = self.head
        i = 1
        r = pt.val
        while pt.next:
            i += 1
            pt = pt.next
            if random.random() < (1 / i):
                r = pt.val
        return r


@pytest.mark.parametrize("values", [([1, 2, 3])])
def test(values):
    obj = Solution(build_list(values))
    cnt = defaultdict(int)
    for i in range(10000):
        cnt[obj.getRandom().val] += 1

    # See if random enough
    print(cnt)


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
