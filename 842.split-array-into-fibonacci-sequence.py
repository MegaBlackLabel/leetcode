#
# @lc app=leetcode id=842 lang=python3
#
# [842] Split Array into Fibonacci Sequence
#

# @lc code=start
from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        
        def backtrack(index: int, path: List[int]) -> bool:
            if index == len(num) and len(path) >= 3:
                return True

            for i in range(index, len(num)):
                if num[index] == '0' and i > index:
                    break

                curr_str = num[index:i + 1]
                curr_num = int(curr_str)

                if curr_num > 2**31 - 1:
                    break

                if len(path) >= 2:
                    if curr_num < path[-1] + path[-2]:
                        continue
                    elif curr_num > path[-1] + path[-2]:
                        break

                path.append(curr_num)
                if backtrack(i + 1, path):
                    return True
                path.pop()

            return False

        result = []
        backtrack(0, result)
        return result
# @lc code=end

