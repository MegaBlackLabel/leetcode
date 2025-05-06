#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def helper(node):
            if not node:
                return "null,"
            return str(node.val) + "," + helper(node.left) + helper(node.right)

        return helper(root)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def helper(nodes):
            if nodes[0] == "null":
                nodes.pop(0)
                return None
            
            node = TreeNode(int(nodes[0]))
            nodes.pop(0)
            node.left = helper(nodes)
            node.right = helper(nodes)
            return node

        nodes = data.split(",")
        root = helper(nodes)
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

