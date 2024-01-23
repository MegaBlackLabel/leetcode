#
# @lc app=leetcode id=1668 lang=python3
#
# [1668] Maximum Repeating Substring
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 1
        
        while word * ans in sequence:
            ans += 1
    
        return ans - 1
# @lc code=end

