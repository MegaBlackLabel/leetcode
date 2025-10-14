#
# @lc app=leetcode id=825 lang=python3
#
# [825] Friends Of Appropriate Ages
#

# @lc code=start
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        count = [0] * 121

        for age in ages:
            count[age] += 1

        result = 0

        for ageA in range(15, 121):
            if count[ageA] == 0:
                continue

            for ageB in range(int(ageA * 0.5 + 7) + 1, ageA + 1):
                if count[ageB] == 0:
                    continue

                result += count[ageA] * (count[ageB] - (1 if ageA == ageB else 0))

        return result
# @lc code=end

