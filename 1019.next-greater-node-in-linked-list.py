#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#

# @lc code=start
# Definition for singly-linked list.

from typing import List, Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack = []
        res = []
        i = 0
        while head:
            res.append(0)
            while stack and stack[-1][0] < head.val:
                res[stack[-1][1]] = head.val
                stack.pop()
            stack.append((head.val, i))
            head = head.next
            i += 1
        return res
# @lc code=end

