#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = Counter(nums)
        return ans.most_common(1)[0][0]


# @lc code=end
