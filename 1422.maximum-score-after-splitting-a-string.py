#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        zeros = 0
        ones = s.count('1')

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1

            ans = max(ans, zeros + ones)

        return ans
# @lc code=end

