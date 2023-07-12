#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        stack = [(root, 1)]

        while stack:
            root, length = stack.pop()
            if not root:
                return 0

            if length > depth:
                depth = length
            if root.right:
                stack.append((root.right, length + 1))
            if root.left:
                stack.append((root.left, length + 1))
        return depth


# @lc code=end
