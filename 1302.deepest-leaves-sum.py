#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        queue = deque([root])
      
        while queue:
            current_level_sum = 0
            level_size = len(queue)
          
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level_sum += current_node.val
              
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
      
        return current_level_sum

# @lc code=end

