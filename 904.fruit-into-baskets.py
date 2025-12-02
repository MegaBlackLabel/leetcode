#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        count = {}
        max_length = 0

        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
# @lc code=end

