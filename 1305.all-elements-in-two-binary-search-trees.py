#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
        def inorder_traversal(root: Optional[TreeNode], elements: List[int]) -> None:
            """
            Perform inorder traversal to collect elements in sorted order.
          
            Args:
                root: Current node in the tree
                elements: List to store elements in sorted order
            """
            if root is None:
                return
          
            # Traverse left subtree
            inorder_traversal(root.left, elements)
            # Process current node
            elements.append(root.val)
            # Traverse right subtree
            inorder_traversal(root.right, elements)
      
        # Collect sorted elements from both trees
        first_tree_elements = []
        second_tree_elements = []
        inorder_traversal(root1, first_tree_elements)
        inorder_traversal(root2, second_tree_elements)
      
        # Get lengths of both lists
        len_first = len(first_tree_elements)
        len_second = len(second_tree_elements)
      
        # Initialize pointers for merging
        pointer_first = 0
        pointer_second = 0
        merged_result = []
      
        # Merge two sorted lists
        while pointer_first < len_first and pointer_second < len_second:
            if first_tree_elements[pointer_first] <= second_tree_elements[pointer_second]:
                merged_result.append(first_tree_elements[pointer_first])
                pointer_first += 1
            else:
                merged_result.append(second_tree_elements[pointer_second])
                pointer_second += 1
      
        # Add remaining elements from first list
        while pointer_first < len_first:
            merged_result.append(first_tree_elements[pointer_first])
            pointer_first += 1
      
        # Add remaining elements from second list
        while pointer_second < len_second:
            merged_result.append(second_tree_elements[pointer_second])
            pointer_second += 1
      
        return merged_result
# @lc code=end

