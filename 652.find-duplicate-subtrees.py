#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
       

        def serialize(node):
            if not node:
                return "#"
            serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            count[serial] += 1
            if count[serial] == 2:
                result.append(node)
            return serial

        count = defaultdict(int)
        result = []
        serialize(root)
        return result
# @lc code=end

