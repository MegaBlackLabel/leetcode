#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return False
            
            left_has_one = dfs(node.left)
            right_has_one = dfs(node.right)
            
            if not left_has_one:
                node.left = None
            if not right_has_one:
                node.right = None
            
            return node.val == 1 or left_has_one or right_has_one
        
        return root if dfs(root) else None
# @lc code=end

