#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        if root.left and root.left.val != root.val: 
            return False
        if root.right and root.right.val != root.val: 
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
# @lc code=end

