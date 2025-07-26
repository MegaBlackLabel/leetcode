#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
from typing import List
from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        count = Counter(nums)
        tails = Counter()

        for num in nums:
            if count[num] == 0:
                continue
            count[num] -= 1

            if tails[num - 1] > 0:
                tails[num - 1] -= 1
                tails[num] += 1
            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                tails[num + 2] += 1
            else:
                return False

        return True
# @lc code=end

