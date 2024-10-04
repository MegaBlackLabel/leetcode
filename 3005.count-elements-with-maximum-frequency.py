#
# @lc app=leetcode id=3005 lang=python3
#
# [3005] Count Elements With Maximum Frequency
#

# @lc code=start
import collections
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        maxFreq = max(count.values())
        return sum(freq == maxFreq for freq in count.values()) * maxFreq
    
# @lc code=end

