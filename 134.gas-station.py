#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = 0
        net = 0
        summ = 0


        for i in range(len(gas)):
            net += gas[i] - cost[i]
            summ += gas[i] - cost[i]
            if summ < 0:
                summ = 0
                ans = i + 1  # Start from the next index.

        return -1 if net < 0 else ans
# @lc code=end

