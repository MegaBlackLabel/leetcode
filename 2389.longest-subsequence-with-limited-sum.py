#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#

# @lc code=start
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        def numOfElementsLessThan(query: int) -> int:
            summ = 0
            for i, num in enumerate(nums):
                summ += num
                if summ > query:
                    return i
        
            return len(nums)

        return [numOfElementsLessThan(query) for query in queries]
# @lc code=end

