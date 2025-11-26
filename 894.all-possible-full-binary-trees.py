#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
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
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        if n % 2 == 0:
            return []

        memo = {}

        def build_trees(nodes: int) -> List[Optional[TreeNode]]:
            if nodes in memo:
                return memo[nodes]

            if nodes == 1:
                return [TreeNode(0)]

            result = []
            for left_nodes in range(1, nodes, 2):
                right_nodes = nodes - 1 - left_nodes
                left_trees = build_trees(left_nodes)
                right_trees = build_trees(right_nodes)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)

            memo[nodes] = result
            return result

        return build_trees(n)
# @lc code=end

