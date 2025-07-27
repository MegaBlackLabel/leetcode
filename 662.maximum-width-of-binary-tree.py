#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        max_width = 0
        queue = [(root, 0)] # (node, index)     
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            last_index = first_index    
            for _ in range(level_length):
                node, index = queue.pop(0)
                last_index = index
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            max_width = max(max_width, last_index - first_index + 1)

        return max_width    

# @lc code=end

