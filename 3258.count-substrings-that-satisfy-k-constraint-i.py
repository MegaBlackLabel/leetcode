#
# @lc app=leetcode id=3258 lang=python3
#
# [3258] Count Substrings That Satisfy K-Constraint I
#

# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        counts = [0, 0]
        
        for r in range(len(s)):
            counts[int(s[r])] += 1
            
            while counts[0] > k and counts[1] > k:
                counts[int(s[l])] -= 1
                l += 1
            
            ans += (r - l + 1)
            
        return ans
# @lc code=end

