#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#

# @lc code=start
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        rows = int((-num_people + (num_people**2 + 8 * num_people**2 * candies)**0.5) / (2 * num_people**2))
        accumN = rows * (rows - 1) * num_people // 2

        for i in range(num_people):
            ans[i] = accumN + rows * (i + 1)

        givenCandies = (num_people**2 * rows**2 + num_people * rows) // 2
        candies -= givenCandies
        lastGiven = rows * num_people
        i = 0

        while candies > 0:
            lastGiven += 1
            actualGiven = min(lastGiven, candies)
            candies -= actualGiven
            ans[i] += actualGiven
            i += 1

        return ans
# @lc code=end

