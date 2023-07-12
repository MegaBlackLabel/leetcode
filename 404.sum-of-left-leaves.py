#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        res = 0
        while stack:
            node = stack.pop(0)
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res


# @lc code=end
