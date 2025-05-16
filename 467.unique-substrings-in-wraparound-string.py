#
# @lc app=leetcode id=467 lang=python3
#
# [467] Unique Substrings in Wraparound String
#

# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        
        max_length = [0] * 26
        n = len(s)
        count = 0

        for i in range(n):
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) + 26) % 26 == 1:
                count += 1
            else:
                count = 1
            
            max_length[ord(s[i]) - ord('a')] = max(max_length[ord(s[i]) - ord('a')], count)

        return sum(max_length)

# @lc code=end

