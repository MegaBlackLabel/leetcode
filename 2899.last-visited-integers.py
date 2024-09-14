#
# @lc app=leetcode id=2899 lang=python3
#
# [2899] Last Visited Integers
#

# @lc code=start
from typing import List


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        ans = []
        n = []
        k = 0

        for num in nums:
            if num == -1:
                k += 1
                ans.append(-1 if k > len(n) else n[-k])
            else:
                k = 0
                n.append(int(num))

        return ans
# @lc code=end

