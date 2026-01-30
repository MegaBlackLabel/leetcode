#
# @lc app=leetcode id=998 lang=python3
#
# [998] Maximum Binary Tree II
#

# @lc code=start
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
# @lc code=end

