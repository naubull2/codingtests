# Use three pointers to reverse the pointing chain in place.
O(1)
O(N)


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(head: ListNode):
    if head is None or head.next is None:  # nothing to reverse
        return head
    curr = head
    fast = head
    prior = None
    while curr is not None:
        curr = fast
        fast = fast.next
        curr.next = prior
        prior = curr
    return curr
