#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num_passengers, from_loc, to_loc in trips:
            events.append((from_loc, num_passengers))   # Pickup event
            events.append((to_loc, -num_passengers))     # Drop-off event
    
        events.sort()  # Sort by location
        current_passengers = 0
    
        for location, passenger_change in events:
            current_passengers += passenger_change
            if current_passengers > capacity:
                return False
    
        return True
# @lc code=end

