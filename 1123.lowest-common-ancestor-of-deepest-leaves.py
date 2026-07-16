#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_lca_and_depth(node):
            if not node:
                return None, 0
            
            left_lca, left_depth = get_lca_and_depth(node.left)
            right_lca, right_depth = get_lca_and_depth(node.right)
            
            # If the deepest leaves are in both subtrees, current node is the LCA
            if left_depth == right_depth:
                return node, left_depth + 1
            
            # If deepest leaves are in the left subtree only
            elif left_depth > right_depth:
                return left_lca, left_depth + 1
            
            # If deepest leaves are in the right subtree only
            else:
                return right_lca, right_depth + 1

        return get_lca_and_depth(root)[0]
    
# @lc code=end

