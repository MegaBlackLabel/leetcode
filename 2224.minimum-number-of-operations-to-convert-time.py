#
# @lc app=leetcode id=2224 lang=python3
#
# [2224] Minimum Number of Operations to Convert Time
#

# @lc code=start
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ops = [60, 15, 5, 1]

        def getMinutes(s: str) -> int:
            return int(s[:2]) * 60 + int(s[3:])

        diff = getMinutes(correct) - getMinutes(current)
        ans = 0

        for op in ops:
            ans += diff // op
            diff %= op

        return ans
# @lc code=end

