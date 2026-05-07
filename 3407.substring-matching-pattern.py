#
# @lc app=leetcode id=3407 lang=python3
#
# [3407] Substring Matching Pattern
#

# @lc code=start
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split('*')
        
        start_idx = s.find(prefix)
        if start_idx == -1:
            return False
        
        return s.find(suffix, start_idx + len(prefix)) != -1
# @lc code=end

