#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        n = len(arr)
        left, right = 0.0, 1.0

        while left < right:
            mid = (left + right) / 2
            count = 0
            max_fraction = 0.0
            p, q = 0, 1
            j = 1

            for i in range(n - 1):
                while j < n and arr[i] > mid * arr[j]:
                    j += 1

                if j == n:
                    break

                count += n - j

                if arr[i] / arr[j] > max_fraction:
                    max_fraction = arr[i] / arr[j]
                    p, q = arr[i], arr[j]

            if count == k:
                return [p, q]
            elif count < k:
                left = mid
            else:
                right = mid

        return []
# @lc code=end

