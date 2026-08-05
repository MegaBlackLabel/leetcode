#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for _ in range(n):
            next_dp = [0] * (target + 1)
            for current_sum in range(target + 1):
                if dp[current_sum] > 0:
                    for face in range(1, k + 1):
                        if current_sum + face <= target:
                            next_dp[current_sum + face] = (next_dp[current_sum + face] + dp[current_sum]) % MOD
            dp = next_dp
            
        return dp[target]
# @lc code=end

