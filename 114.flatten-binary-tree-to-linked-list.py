#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        while root:
            if root.left:
                rightmost = root.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        
# @lc code=end

