from heapq import heappop, heappush


"""
Implementing Custom class with __lt__ comparator with desired order.
Without a custom class, base implementation from heapq is a minheap, which would be like:

class Node:
    def __init__(self, val:int):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

From here, we can implement a custom node class to create a desired
priority heap
"""

# Example) A max heap where larger score is considered,
# for ties in scores, consider lexiographically lower name is considered.

class MaxNode:
    def __init__(self, name:str, score:int):
        self.name = name
        self.score = score

    def __lt__(self, other):
        if self.score == other.score:
            return self.name < other.name
        return self.score > other.score

    def __repr__(self):
        return f"{self.name}: {self.score}"

max_heap = []
heappush(max_heap, MaxNode("Bradford", 2))
heappush(max_heap, MaxNode("Bradford", 3))
heappush(max_heap, MaxNode("Alps", 3))

print(max_heap[0])

