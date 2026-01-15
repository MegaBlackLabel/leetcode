#
# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
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
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        
        res = []
        i = 0

        def dfs(node):
            nonlocal i
            if not node:
                return True
            if node.val != voyage[i]:
                return False
            i += 1
            if (node.left and node.left.val != voyage[i]):
                res.append(node.val)
                node.left, node.right = node.right, node.left
            return dfs(node.left) and dfs(node.right)

        if dfs(root):
            return res
        else:
            return [-1]
# @lc code=end

