#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix_sum.get(curr_sum - targetSum, 0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
            
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            prefix_sum[curr_sum] -= 1
            
            return count
        
        prefix_sum = {0: 1}
        return dfs(root, 0)
# @lc code=end

