#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        nums = [1]
        indices = [0] * k

        while len(nums) < n:
            next_num = min([nums[indices[i]] * primes[i] for i in range(k)])
            nums.append(next_num)
            for i in range(k):
                if nums[indices[i]] * primes[i] == next_num:
                    indices[i] += 1

        return nums[-1]


# @lc code=end

