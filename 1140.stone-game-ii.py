#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#

# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        suff_sum = piles.copy()
        for i in range(len(piles) - 2, -1, -1):
            suff_sum[i] += suff_sum[i + 1]

        def dp(i: int, m: int) -> int:
            if i + 2 * m >= len(piles):
                return suff_sum[i]
            if (i, m) in memo:
                return memo[(i, m)]

            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, suff_sum[i] - dp(i + x, max(m, x)))

            memo[(i, m)] = res
            return res

        return dp(0, 1)
# @lc code=end

