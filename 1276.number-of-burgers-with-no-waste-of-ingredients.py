#
# @lc app=leetcode id=1276 lang=python3
#
# [1276] Number of Burgers with No Waste of Ingredients
#

# @lc code=start
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        difference = 4 * cheeseSlices - tomatoSlices
        num_small_burgers = difference // 2

        num_jumbo_burgers = cheeseSlices - num_small_burgers

        if difference % 2 != 0 or num_small_burgers < 0 or num_jumbo_burgers < 0:
            return []
      
        return [num_jumbo_burgers, num_small_burgers]
    
# @lc code=end

