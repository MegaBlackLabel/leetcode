#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#

# @lc code=start
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curr = 0

        for num in nums:
            curr = (curr * 2 + num) % 5
            ans.append(curr % 5 == 0)

        return ans
# @lc code=end

