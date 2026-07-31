#
# @lc app=leetcode id=1145 lang=python3
#
# [1145] Binary Tree Coloring Game
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
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.left_count = 0
        self.right_count = 0
        
        def count_nodes(node):
            if not node:
                return 0
            
            left = count_nodes(node.left)
            right = count_nodes(node.right)
            
            if node.val == x:
                self.left_count = left
                self.right_count = right
                
            return left + right + 1

        count_nodes(root)
        
        parent_count = n - self.left_count - self.right_count - 1
        winning_threshold = n // 2
        
        return (self.left_count > winning_threshold or 
                self.right_count > winning_threshold or 
                parent_count > winning_threshold)
# @lc code=end

