#
# @lc app=leetcode id=1343 lang=python3
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target_sum = k * threshold

        current_sum = sum(arr[:k])
        count = 1 if current_sum >= target_sum else 0

        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]

            if current_sum >= target_sum:
                count += 1

        return count
# @lc code=end

