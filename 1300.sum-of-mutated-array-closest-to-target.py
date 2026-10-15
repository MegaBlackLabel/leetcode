#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#

# @lc code=start
from bisect import bisect_right
from itertools import accumulate


class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix_sums = list(accumulate(arr, initial=0))

        def calculate_sum(value):
            index = bisect_right(arr, value)
            return prefix_sums[index] + (n - index) * value

        left, right = 0, max(arr)
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if calculate_sum(mid) >= target:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        if first_true_index == -1:
            return max(arr)

        if first_true_index == 0:
            return 0

        if abs(calculate_sum(first_true_index - 1) - target) <= abs(calculate_sum(first_true_index) - target):
            return first_true_index - 1
        return first_true_index
# @lc code=end

