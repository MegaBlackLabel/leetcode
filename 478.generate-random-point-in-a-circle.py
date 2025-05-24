#
# @lc app=leetcode id=478 lang=python3
#
# [478] Generate Random Point in a Circle
#

# @lc code=start
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        
        """
        Initialize the circle with radius and center (x_center, y_center).
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        """
        Return a random point in the circle.
        The point is represented as an array of length 2, where the first element is the x-coordinate and the second element is the y-coordinate.
        """
        import random
        import math

        # Generate a random angle and radius
        angle = random.uniform(0, 2 * math.pi)
        r = math.sqrt(random.uniform(0, self.radius ** 2))

        # Calculate the x and y coordinates
        x = self.x_center + r * math.cos(angle)
        y = self.y_center + r * math.sin(angle)

        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end

