#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(None)
        res.next = head
        node = res

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return res.next


# @lc code=end
