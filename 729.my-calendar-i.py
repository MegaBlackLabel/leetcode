#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.bookings:
            if start < endTime and startTime < end:
                return False
        self.bookings.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

