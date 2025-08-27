#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start
from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.booking_counts = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:

        self.booking_counts[startTime] = self.booking_counts.get(startTime, 0) + 1
        self.booking_counts[endTime] = self.booking_counts.get(endTime, 0) - 1
        running_sum = 0

        for count in self.booking_counts.values():
            running_sum += count

         
            if running_sum > 2:
                self.booking_counts[startTime] -= 1
                self.booking_counts[endTime] += 1
                return False

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

