#
# @lc app=leetcode id=3477 lang=python3
#
# [3477] Fruits Into Baskets II
#

# @lc code=start
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        is_used = [False] * n
        unplaced_count = len(fruits)

        for fruit_size in fruits:
            for basket_index, basket_capacity in enumerate(baskets):
                if basket_capacity >= fruit_size and not is_used[basket_index]:
                    is_used[basket_index] = True
                    unplaced_count -= 1
                    break

        return unplaced_count
# @lc code=end

