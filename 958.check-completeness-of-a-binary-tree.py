#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = [root]
        end = False

        while queue:
            node = queue.pop(0)

            if not node:
                end = True
            else:
                if end:
                    return False

                queue.append(node.left)
                queue.append(node.right)

        return True
# @lc code=end

