#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0

        for i, ticket in enumerate(tickets):
            if i <= k:
                ans += min(ticket, tickets[k])
            else:
                ans += min(ticket, tickets[k] - 1)

        return ans
# @lc code=end

