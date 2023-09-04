#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        def inOrder(root, res):
            if not root:
                return
            inOrder(root.left, res)
            res.append(root.val)
            inOrder(root.right, res)
            return res
        
        array = inOrder(root, [])
        root = cur = TreeNode(array[0])
        for i in range(1, len(array)):
            cur.right = TreeNode(array[i])
            cur = cur.right
        return root
# @lc code=end

