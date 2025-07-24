#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#

# @lc code=start
# Definition for a binary tree node.

from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def maxHeight(root: TreeNode | None) -> int:
            if not root:
                return 0
            return 1 + max(maxHeight(root.left), maxHeight(root.right))

        def dfs(root: TreeNode | None, row: int, left: int, right: int) -> None:
            if not root:
                return

            mid = (left + right) // 2
            ans[row][mid] = str(root.val)
            dfs(root.left, row + 1, left, mid - 1)
            dfs(root.right, row + 1, mid + 1, right)

        m = maxHeight(root)
        n = pow(2, m) - 1
        ans = [[''] * n for _ in range(m)]
        dfs(root, 0, 0, len(ans[0]) - 1)
        return ans
# @lc code=end

