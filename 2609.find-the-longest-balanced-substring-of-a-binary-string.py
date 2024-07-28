#
# @lc app=leetcode id=2609 lang=python3
#
# [2609] Find the Longest Balanced Substring of a Binary String
#

# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0

        i = 0
        
        while i < len(s):
            zeros = 0
            ones = 0
            while i < len(s) and s[i] == '0':
                zeros += 1
                i += 1
            while i < len(s) and s[i] == '1':
                ones += 1
                i += 1
            ans = max(ans, min(zeros, ones))

        return ans * 2
# @lc code=end

