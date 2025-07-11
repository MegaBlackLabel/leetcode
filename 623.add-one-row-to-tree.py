#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, root)

        def dfs(node, current_depth):
            if not node:
                return
            if current_depth == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
            else:
                dfs(node.left, current_depth + 1)
                dfs(node.right, current_depth + 1)

        dfs(root, 1)
        return root
# @lc code=end

