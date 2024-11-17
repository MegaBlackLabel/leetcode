#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        tail = head
        length = 1
        
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head  # Circle the list.

        t = length - k % length
        
        for _ in range(t):
            tail = tail.next
        newHead = tail.next
        tail.next = None

        return newHead
# @lc code=end

