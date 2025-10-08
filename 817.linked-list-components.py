#
# @lc app=leetcode id=817 lang=python3
#
# [817] Linked List Components
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        nums_set = set(nums)
        count = 0
        in_component = False
        
        current = head
        while current:
            if current.val in nums_set:
                if not in_component:
                    count += 1
                    in_component = True
            else:
                in_component = False
            current = current.next
        
        return count
# @lc code=end

