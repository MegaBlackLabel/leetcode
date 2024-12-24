#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root  # the node that is above the current needling

        while node:
            dummy = Node(0)
            needle = dummy
            while node:
                if node.left:  # Needle the left child.
                    needle.next = node.left
                    needle = needle.next
                if node.right:  # Needle the right child.
                    needle.next = node.right
                    needle = needle.next
                node = node.next
            node = dummy.next  # Move the node to the next level.

        return root
# @lc code=end

