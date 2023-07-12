#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []

        stack.append(p)
        stack.append(q)

        while stack:

            a = stack.pop()
            b = stack.pop()

            if a is None and b is None:
                continue

            if (
                (a is not None and b is None)
                or (a is None and b is not None)
                or (a.val != b.val)
            ):
                return False

            stack.append(a.left)
            stack.append(b.left)

            stack.append(a.right)
            stack.append(b.right)

        return True


# @lc code=end
