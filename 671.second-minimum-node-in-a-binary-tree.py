#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return -1
        
        self.res = float("inf")
        self.min = root.val
        self.inOrder(root)
        
        return self.res if self.res != float("inf") else -1

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.min < root.val < self.res:
            self.res = root.val
        self.inOrder(root.right)

# @lc code=end

