#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode], depth: int) -> tuple[int, Optional[TreeNode]]:
            if not node:
                return depth, None

            left_depth, left_node = dfs(node.left, depth + 1)
            right_depth, right_node = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                return left_depth, left_node
            elif right_depth > left_depth:
                return right_depth, right_node
            else:
                return left_depth, node

        return dfs(root, 0)[1]

# @lc code=end

