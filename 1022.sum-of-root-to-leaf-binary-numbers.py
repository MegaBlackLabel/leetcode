#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root: 
             return 0

        self.res = 0
        self.dfs(root, str(root.val))
        return self.res

    def dfs(self, node, cur_str):
        if not node.left and not node.right:
            self.res += int(cur_str, 2)
            return 
        
        if node.left: 
            self.dfs(node.left, cur_str + str(node.left.val))
        if node.right: 
            self.dfs(node.right, cur_str + str(node.right.val))
# @lc code=end

