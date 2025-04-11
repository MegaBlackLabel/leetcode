#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
import collections
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.p = collections.defaultdict(list)
        for i, d in enumerate(nums):
            self.p[d].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.p[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

