#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#

# @lc code=start
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        res = []
        n = len(arr)

        def flip(k: int) -> None:
            i, j = 0, k
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        for size in range(n, 1, -1):
            max_index = arr.index(max(arr[:size]))
            if max_index != size - 1:
                if max_index != 0:
                    flip(max_index)
                    res.append(max_index + 1)
                flip(size - 1)
                res.append(size)

        return res
# @lc code=end

