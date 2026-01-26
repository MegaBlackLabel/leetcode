#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#
from typing import Optional

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        self.smallest_string = "~" # Initialize with a string greater than any possible result

        def dfs(node, current_string):
            if not node:
                return
            
            # Prepend the current node's character to build string from leaf to root
            current_string = chr(ord('a') + node.val) + current_string

            # If it's a leaf node, compare and update the smallest string found so far
            if not node.left and not node.right:
                if current_string < self.smallest_string:
                    self.smallest_string = current_string
                return
            
            # Recursively call DFS for left and right children
            if node.left:
                dfs(node.left, current_string)
            if node.right:
                dfs(node.right, current_string)

        dfs(root, "")
        return self.smallest_string
# @lc code=end

