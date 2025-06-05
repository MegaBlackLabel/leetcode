#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [1] + [0] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
# @lc code=end

