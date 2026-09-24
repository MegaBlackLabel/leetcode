#
# @lc app=leetcode id=1261 lang=python3
#
# [1261] Find Elements in a Contaminated Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class FindElements:

    def __init__(self, root: TreeNode | None):
        self.values = set()
        self._dfs(root, 0)

    def _dfs(self, node: Optional[TreeNode], val: int):
        if not node:
            return
        node.val = val
        self.values.add(val)
        self._dfs(node.left, 2 * val + 1)
        self._dfs(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end

