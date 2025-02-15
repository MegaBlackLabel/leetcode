#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = collections.deque([root])
        isLeftToRight = True

        while q:
            size = len(q)
            currLevel = [0] * size
            for i in range(size):
                node = q.popleft()
                index = i if isLeftToRight else size - i - 1
                currLevel[index] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(currLevel)
            isLeftToRight = not isLeftToRight

        return ans
# @lc code=end

