#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#

# @lc code=start
class Solution:
    def knightDialer(self, n: int) -> int:
        
        MOD = 10**9 + 7
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        dp = [1] * 10

        for _ in range(n - 1):
            new_dp = [0] * 10
            for digit in range(10):
                for move in moves[digit]:
                    new_dp[move] = (new_dp[move] + dp[digit]) % MOD
            dp = new_dp

        return sum(dp) % MOD
# @lc code=end

