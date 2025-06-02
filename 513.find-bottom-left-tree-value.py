#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        bottom_left_value = root.val

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == 0:
                    bottom_left_value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return bottom_left_value        

# @lc code=end

