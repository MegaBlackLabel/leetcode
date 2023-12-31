#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        h1 = headA
        h2 = headB

        while h1 != h2:
            if not h1:
                h1 = headB
            else:
                h1 = h1.next

            if not h2:
                h2 = headA
            else:
                h2 = h2.next

        return h1


# @lc code=end
