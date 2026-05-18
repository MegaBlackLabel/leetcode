#
# @lc app=leetcode id=3456 lang=python3
#
# [3456] Find Special Substring of Length K
#

# @lc code=start

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        count = 1
        n = len(s)
        
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
            else:
                if count == k:
                    return True
                count = 1
        
        return count == k
# @lc code=end

