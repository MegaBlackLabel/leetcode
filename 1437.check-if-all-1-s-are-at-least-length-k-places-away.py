#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#

# @lc code=start
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True

        n = len(nums)

        curr = 0
        next = 1

        while curr < n and next < n:
            if nums[next] == 1:
                if nums[curr] == 1 and next - curr <= k:
                    return False
                curr = next
            next += 1

        return True
# @lc code=end

