#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix_sum = 0
        seen = {}
        
        curr = dummy
        while curr:
            prefix_sum += curr.val
            seen[prefix_sum] = curr
            curr = curr.next
            
        prefix_sum = 0
        curr = dummy
        while curr:
            prefix_sum += curr.val
            curr.next = seen[prefix_sum].next
            curr = curr.next
            
        return dummy.next
# @lc code=end

