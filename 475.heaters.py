#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()

        radius = 0
        heater_index = 0

        for house in houses:
            while (heater_index < len(heaters) - 1 and
                   abs(house - heaters[heater_index]) >= abs(house - heaters[heater_index + 1])):
                heater_index += 1
            
            radius = max(radius, abs(house - heaters[heater_index]))

        return radius
# @lc code=end

