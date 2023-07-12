#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
from typing import Optional, List  # Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        if root is None:
            return res

        stack = [root, str(root.val) + "->"]
        path = ""

        while stack:
            path = stack.pop()
            node = stack.pop()

            if node.left is None and node.right is None:
                res.append(path[:-2])

            if node.right:
                stack.append(node.right)
                stack.append(path + str(node.right.val) + "->")

            if node.left:
                stack.append(node.left)
                stack.append(path + str(node.left.val) + "->")

        return res


# @lc code=end
