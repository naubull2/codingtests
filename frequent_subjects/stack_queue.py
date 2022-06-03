import sys

#####################
# queue with 2 stacks
#####################
class StackQueue(object):
    """
    O(n) for either push / pop
    Following code will go with O(n) for pop

    Either use a separate stack to reverse the order,
    or use a function call stack to reverse the order.
    Both ways will induce two "stack" usages, though the function call stack
    is much more inefficient space complexity-wise
    """
    def __init__(self):
        self.stack = []
        self.rev = []
        self.front = None

    def push(self, val):
        if not self.stack:
            self.front = val
        self.stack.append(val)

    def pop(self):
        while self.stack:
            self.rev.append(self.stack.pop())

        item = self.rev.pop()
        if self.rev:
            self.front = self.rev[-1]
        while self.rev:
            self.stack.append(self.rev.pop())

        return item

    def peek(self):
        return self.front

    def __len__(self):
        return len(self.stack)

    def pop_single_stack(self):
        def deque():
            val = self.stack.pop()
            if not self.stack: # return the final value
                return val

            # other wise go deeper
            item = deque()

            # restore once back to this step
            self.stack.append(val)
            return item
        return deque()


q = StackQueue()

vals = [1,2,3,4,5]
for v in vals:
    q.push(v)

while q:
    print(q.pop_single_stack())    


