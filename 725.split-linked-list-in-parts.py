#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Determine the size of each part and the number of longer parts
        part_size = length // k
        extra_nodes = length % k

        parts = []
        current = head

        for i in range(k):
            part_head = current
            part_length = part_size + (1 if i < extra_nodes else 0)

            for j in range(part_length - 1):
                if current:
                    current = current.next

            if current:
                next_part_head = current.next
                current.next = None
                current = next_part_head

            parts.append(part_head)

        return parts
# @lc code=end

