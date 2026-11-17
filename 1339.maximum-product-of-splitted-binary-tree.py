#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
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
    def maxProduct(self, root: TreeNode | None) -> int:
        """
        Find the maximum product of sums of two subtrees formed by removing one edge.
        The result is returned modulo 10^9 + 7.
        """
      
        def calculate_total_sum(node: Optional[TreeNode]) -> int:
            """
            Calculate the sum of all node values in the tree.
          
            Args:
                node: The root of the tree/subtree
              
            Returns:
                The sum of all node values in the tree rooted at 'node'
            """
            if node is None:
                return 0
          
            return node.val + calculate_total_sum(node.left) + calculate_total_sum(node.right)
      
        def find_max_product(node: Optional[TreeNode]) -> int:
            """
            Traverse the tree and find the maximum product by trying each possible edge removal.
          
            Args:
                node: The current node being processed
              
            Returns:
                The sum of the subtree rooted at 'node'
            """
            if node is None:
                return 0
          
            subtree_sum = node.val + find_max_product(node.left) + find_max_product(node.right)
          
            nonlocal max_product, total_sum
            if subtree_sum < total_sum:
                max_product = max(max_product, subtree_sum * (total_sum - subtree_sum))
          
            return subtree_sum
      
        MOD = 10**9 + 7
      
        total_sum = calculate_total_sum(root)
        max_product = 0
        find_max_product(root)
      
        return max_product % MOD
# @lc code=end

