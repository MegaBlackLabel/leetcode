#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
      
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            missing_until_mid = arr[mid] - mid - 1
          
            if missing_until_mid >= k:
                right = mid
            else:
                left = mid + 1


        missing_until_left_minus_one = arr[left - 1] - (left - 1) - 1
        res = arr[left - 1] + k - missing_until_left_minus_one
        return res

# @lc code=end

