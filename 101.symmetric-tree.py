#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root, root)

    def dfs(self, left, right):
        if left and right:
            return (
                left.val == right.val
                and self.dfs(left.left, right.right)
                and self.dfs(left.right, right.left)
            )
        else:
            return left == right


# @lc code=end
