#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:

        def dfs(node: TreeNode, parent_val: int) -> int:
            """
            Depth-first search to find sum of nodes with even grandparents.
          
            Args:
                node: Current node being processed
                parent_val: Value of the parent node (potential grandparent for children)
              
            Returns:
                Sum of nodes with even grandparents in this subtree
            """
            if node is None:
                return 0
          
            total_sum = dfs(node.left, node.val) + dfs(node.right, node.val)
          

            if parent_val % 2 == 0:
                if node.left:
                    total_sum += node.left.val
                if node.right:
                    total_sum += node.right.val
          
            return total_sum
      
        return dfs(root, 1)
# @lc code=end

