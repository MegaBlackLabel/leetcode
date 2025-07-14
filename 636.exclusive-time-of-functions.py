#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        stack = []
        result = [0] * n
        prev_time = 0

        for log in logs:
            id_str, type_str, time_str = log.split(':')
            id_ = int(id_str)
            time = int(time_str)

            if type_str == 'start':
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(id_)
                prev_time = time
            else:
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return result
# @lc code=end

