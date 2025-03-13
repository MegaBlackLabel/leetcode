#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slot = 1
        
        for node in nodes:
            slot -= 1
            if slot < 0:
                return False
            if node != '#':
                slot += 2
        
        return slot == 0

# @lc code=end

