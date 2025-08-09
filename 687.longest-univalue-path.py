#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            left_path = left_length + 1 if node.left and node.left.val == node.val else 0
            right_path = right_length + 1 if node.right and node.right.val == node.val else 0
            
            self.max_length = max(self.max_length, left_path + right_path)
            
            return max(left_path, right_path)

        self.max_length = 0
        dfs(root)
        return self.max_length
# @lc code=end

