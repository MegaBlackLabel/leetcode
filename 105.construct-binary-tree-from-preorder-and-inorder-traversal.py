#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        val_inorder_idx = {}
        for i, num in enumerate(inorder):
            val_inorder_idx[num] = i

        def build_helper(preorder_left_idx, preorder_right_idx, inorder_left_idx, inorder_right_idx, node_count):
            if node_count < 1:
                return None
            val = preorder[preorder_left_idx]
            node = TreeNode(val)
            inorder_mid_idx = val_inorder_idx[val]
            left_tree_count = inorder_mid_idx - inorder_left_idx
            right_tree_count = node_count - left_tree_count - 1
            node.left = build_helper(preorder_left_idx + 1, preorder_left_idx + left_tree_count, inorder_left_idx, inorder_mid_idx - 1, left_tree_count)
            node.right = build_helper(preorder_left_idx + left_tree_count + 1, preorder_right_idx, inorder_mid_idx + 1, inorder_right_idx, right_tree_count)
            return node

        return build_helper(0, n - 1, 0, n - 1, n)    

# @lc code=end

