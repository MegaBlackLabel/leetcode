#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode], acc: int) -> int:
            if not node:
                return acc
            
            # Traverse the right subtree first
            acc = dfs(node.right, acc)
            
            # Update the current node's value
            node.val += acc
            
            # Traverse the left subtree
            return dfs(node.left, node.val)

        dfs(root, 0)
        return root
# @lc code=end

