#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = nums.count(target)
        lessThan = sum(num < target for num in nums)
        return [i for i in range(lessThan, lessThan + count)]
# @lc code=end

