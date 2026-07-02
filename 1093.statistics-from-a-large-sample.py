#
# @lc app=leetcode id=1093 lang=python3
#
# [1093] Statistics from a Large Sample
#

# @lc code=start
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = -1.0
        maximum = -1.0
        total_sum = 0.0
        total_count = 0
        max_freq = 0
        mode = 0.0

        for i in range(256):
            if count[i] > 0:
                if minimum == -1.0:
                    minimum = float(i)
                maximum = float(i)

        for i in range(256):
            if count[i] > 0:
                total_sum += float(i) * count[i]
                total_count += count[i]

                # Update mode
                if count[i] > max_freq:
                    max_freq = count[i]
                    mode = float(i)

        mean = total_sum / total_count

        median = 0.0
        mid1 = (total_count + 1) // 2
        mid2 = (total_count + 2) // 2

        curr_count = 0
        med1_val = -1
        med2_val = -1

        for i in range(256):
            curr_count += count[i]

            if med1_val == -1 and curr_count >= mid1:
                med1_val = i

            if med2_val == -1 and curr_count >= mid2:
                med2_val = i
                break

        median = (med1_val + med2_val) / 2.0

        return [minimum, maximum, mean, median, mode]
# @lc code=end

