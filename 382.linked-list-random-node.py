#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        
        """
        :type head: ListNode
        """
        self.head = head
        self.size = 0
        current = head
        while current:
            self.size += 1
            current = current.next

    def getRandom(self) -> int:
        
        """
        :rtype: int
        """
        import random
        index = random.randint(0, self.size - 1)
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

