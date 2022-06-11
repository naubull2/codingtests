# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	int get(int key) Return the value of the key if the key exists, otherwise return -1.
	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:

	1 <= capacity <= 3000
	0 <= key <= 104
	0 <= value <= 105
	At most 2 * 105 calls will be made to get and put.
"""
import pytest

class Node(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = self
        self.next = self

        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.table = dict()
        self.head = Node()
        self.size = capacity
        capacity -= 1
        # insert until we have capacity amount of nodes in the chain
        while capacity > 0:
            self.make_node_tail(Node())
            capacity -= 1

    def get(self, key: int) -> int:
        # find and get the value (-1 if don't exist)
        node = self.table.get(key, None)
        if node is None:
            return -1
        
        # update the node to be the new head
        self.make_node_tail(node)
        self.head = node
        return self.head.val
        

    def put(self, key: int, value: int) -> None:
        # if Key exist, update
        # else: evict and put new key-value
        if key in self.table:
            node = self.table[key]
            node.val = value

            if self.head != node:
                self.make_node_tail(node)
                self.head = node
            return
        
        # 1. evict the tail node's key in the hash table (if not exist, else update only)
        node = self.head.prev
        self.table.pop(node.key, None)
        
        # 2. put the new key value in to the tail of the chain,
        node.key, node.val = key, value
        self.make_node_tail(node)
        
        # 3. the tail becomes the new head (recently updated)
        self.table[key] = node
        self.head = node
        
    
    def make_node_tail(self, node):
        # 1. break node out
        node.prev.next = node.next
        node.next.prev = node.prev
        # 2. put node in 
        node.prev = self.head.prev
        node.next = self.head.prev.next
        # 3. connect head / tail to node
        node.next.prev = node
        node.prev.next = node



@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
     [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
     [None, None, None, 1, None, -1, None, -1, 3, 4]),

    (["LRUCache", "put", "put", "get", "get", "put", "get", "get", "get"],
     [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]],
     [None, None, None, 2, 1, None, 1, -1, 3])
])
def test(commands, arguments, expecteds):
    obj = LRUCache(*arguments[0])
    for cmd, arg, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*arg)

if __name__ == '__main__':
    sys.exit(pytest.main(['-s', '-v'] + sys.argv))
