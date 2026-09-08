#
# @lc app=leetcode id=1234 lang=python3
#
# [1234] Replace the Substring for Balanced String
#

# @lc code=start
from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        limit = n // 4
        count = Counter(s)
        
        if all(count[c] <= limit for c in 'QWER'):
            return 0
            
        ans = n
        left = 0
        
        for right in range(n):
            count[s[right]] -= 1
            while left < n and all(count[c] <= limit for c in 'QWER'):
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1
                
        return ans
# @lc code=end

