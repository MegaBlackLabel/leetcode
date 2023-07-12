#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            # Falseを返す
            return False

        if not root.left and not root.right and root.val == targetSum:
            # Trueを返す
            return True

        targetSum = targetSum - root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


# @lc code=end
