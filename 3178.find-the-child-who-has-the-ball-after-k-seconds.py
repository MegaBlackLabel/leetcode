#
# @lc app=leetcode id=3178 lang=python3
#
# [3178] Find the Child Who Has the Ball After K Seconds
#

# @lc code=start
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        passes_per_segment = n - 1
        
        k, mod = divmod(k, passes_per_segment)
        
        if k % 2 == 0:
            return mod
        else:
            return n - 1 - mod
# @lc code=end

