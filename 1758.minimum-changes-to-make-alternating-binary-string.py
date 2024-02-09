#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        a = sum(int(c) == i % 2 for i, c in enumerate(s))
        b = len(s) - a
    
        return min(a, b)
# @lc code=end

