#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n == 0:
            return 1

        if n == 1:
            return 10

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 9

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (11 - i)

        return sum(dp)
# @lc code=end

