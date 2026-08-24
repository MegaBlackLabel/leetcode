#
# @lc app=leetcode id=1191 lang=python3
#
# [1191] K-Concatenation Maximum Sum
#

# @lc code=start
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        def kadane(sub_arr: list[int]) -> int:
            """Standard Kadane's algorithm allowing an empty subarray (min sum = 0)."""
            max_so_far = 0
            current_max = 0
            for num in sub_arr:
                current_max = max(num, current_max + num)
                max_so_far = max(max_so_far, current_max)
            return max_so_far

        if k == 1:
            return kadane(arr) % MOD
        
        double_arr_max = kadane(arr * 2)
        total_sum = sum(arr)
        
        if total_sum > 0:
            return (double_arr_max + (k - 2) * total_sum) % MOD
        else:
            return double_arr_max % MOD
# @lc code=end

