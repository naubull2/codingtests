#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from collections import deque
from typing import List, Union


class Tree(object):
    def __init__(self, val=float('inf')):
        self.val = val
        self.cnt = 1
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, node: Union['Tree', int]):
        if not isinstance(node, Tree):
            node = Tree(node)
        if node.val < self.val:
            if self.left:
                return self.left.insert(node)
            else:
                self.left = node
                node.parent = self
                return node
        elif node.val > self.val:
            if self.right:
                return self.right.insert(node)
            else:
                self.right = node
                node.parent = self
                return node
        else:
            self.cnt += 1
            return self

    def find(self, val):
        if val == self.val:
            return self
        elif val < self.val and self.left:
            return self.left.find(val)
        elif val > self.val and self.right:
            return self.right.find(val)

    def remove_val(self, val):
        n = self.find(val)
        if n:
            return n.remove()
        return False

    def remove(self):
        if self.cnt > 1:
            self.cnt -= 1
            return True
        if self.is_leaf():
            if not self.parent:
                print('You are trying to remove the last node of the tree')
                return False
            elif self.parent.left == self:
                self.parent.left = None
            elif self.parent.right == self:
                self.parent.right = None
            return True
        else:
            if self.right:
                n = self.right.min()
            else:
                n = self.left.max()
            self.val = n.val
            self.cnt = n.cnt
            n.remove()
            return True

    def is_leaf(self):
        return not (self.left or self.right)

    def is_root(self):
        return not self.root

    def min(self):
        if self.left:
            return self.left.min()
        return self

    def max(self):
        if self.right:
            return self.right.max()
        return self

    def successor(self):
        if self.cnt > 1:
            return self
        if self.right:
            return self.right.min()
        n = self
        while n.parent:
            if n.parent.left == n:
                return n.parent
            n = n.parent
        return None

    def predecessor(self):
        if self.cnt > 1:
            return self
        if self.left:
            return self.left.max()
        n = self
        while n.parent:
            if n.parent.right == n:
                return n.parent
            n = n.parent
        return None

    def __repr__(self):
        rep = ''
        left_padding = 0
        right_padding = 0
        left = str(self.left).split('\n') if self.left else []
        if left:
            rep += '/'
            left_padding = len(left[0])
        rep += str((self.val, self.cnt))
        right = str(self.right).split('\n') if self.right else []
        if right:
            rep += '\\'
            right_padding = len(right[0])
        from itertools import zip_longest
        lines = [' ' * left_padding + rep + ' ' * right_padding,
                 *[(l if l else ' ' * left_padding) + ' ' * len(rep) + (r if r else ' ' * right_padding)
                   for l, r in zip_longest(left, right)]]
        return '\n'.join(lines)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        from itertools import zip_longest
        left_lines = repr(self.left).split('\n') if self.left else []
        right_lines = repr(self.right).split('\n') if self.right else []
        node_padding = len(repr(self.val)) + 2
        left_padding = len(left_lines[0]) if left_lines else 0
        right_padding = len(right_lines[0]) if right_lines else 0
        lines = [' '*left_padding + rf'({self.val})' + ' '*right_padding]
        for ll, rl in zip_longest(left_lines, right_lines):
            if ll is not None:
                lines.append(ll + ' '*node_padding + (rl or ''))
            else:
                lines.append(' '*(node_padding + left_padding) + (rl or ''))
        return '\n'.join(lines)

    def __eq__(self, other):
        return other.val == self.val \
            and other.left == self.left \
            and other.right == self.right


def build_tree(lst, constructor=TreeNode):
    if not lst:
        return None
    root = constructor(lst[0])
    queue = [root]
    att = ['left', 'right']
    cur = 0
    for x in lst[1:]:
        node = constructor(x) if x is not None else None
        setattr(queue[0], att[cur], node)
        if cur:
            queue.pop(0)
        if node:
            queue.append(node)
        cur += 1
        cur %= 2
    return root


def serialize_tree(root):
    ret = []
    if not root:
        return ret
    level = [root]
    while level:
        new_level = []
        for node in level:
            if node is None:
                ret.append(node)
            else:
                ret.append(node.val)
                new_level.append(node.left)
                new_level.append(node.right)
        level = new_level
    while ret and ret[-1] is None:
        ret.pop()
    return ret


def print_tree(root):
    from itertools import zip_longest
    def build_lines(root):
        if not root:
            return [''], 0
        left, lw = build_lines(root.left)
        lp = ' '*lw
        right, rw = build_lines(root.right)
        rp = ' '*rw
        s = str(root)
        subs = [(l if l else lp) + ' '*len(s) + (r if r else rp) for l, r in zip_longest(left, right)]
        first_line = lp + s + rp
        return [first_line] + subs, len(first_line)
    lines, _ = build_lines(root)
    print('\n'.join(lines))


def build_bst(lst):
    def insert(root, node):
        if node.val < root.val:
            if not root.left:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if not root.right:
                root.right = node
            else:
                insert(root.right, node)
    if not lst:
        return None
    nodes = [TreeNode(x) for x in lst]
    root = nodes[0]
    for node in nodes[1:]:
        insert(root, node)
    return root

