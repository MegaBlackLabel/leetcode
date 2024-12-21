#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, current_sum):
            nonlocal targetSum, paths, current_path
            if node is None:
                return

            current_sum += node.val
            current_path.append(node.val)

            if node.left is None and node.right is None and current_sum == targetSum:
                paths.append(current_path[:])

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
          
            current_path.pop()

        paths = []
        current_path = []
        dfs(root, 0)
        return paths
# @lc code=end

