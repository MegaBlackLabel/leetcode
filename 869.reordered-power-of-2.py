#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        from collections import Counter

        def digit_count(x):
            return Counter(str(x))

        n_count = digit_count(n)

        for i in range(31):  # 2^0 to 2^30
            if digit_count(1 << i) == n_count:
                return True

        return False
# @lc code=end

