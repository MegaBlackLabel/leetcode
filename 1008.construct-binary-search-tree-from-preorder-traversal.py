#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            node = TreeNode(value)

            if value < stack[-1].val:
                stack[-1].left = node
            else:
                parent = None
                while stack and stack[-1].val < value:
                    parent = stack.pop()
                parent.right = node

            stack.append(node)

        return root
# @lc code=end

