#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
import random
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        median = self._findKthLargest(nums, (n + 1) // 2)

        def A(i: int):
            return (1 + 2 * i) % (n | 1)

        i = 0
        j = 0
        k = n - 1

        while i <= k:
            if nums[A(i)] > median:
                nums[A(i)], nums[A(j)] = nums[A(j)], nums[A(i)]
                i, j = i + 1, j + 1
            elif nums[A(i)] < median:
                nums[A(i)], nums[A(k)] = nums[A(k)], nums[A(i)]
                k -= 1
            else:
                i += 1


    def _findKthLargest(self, nums: list[int], k: int) -> int:
        def quickSelect(l: int, r: int, k: int) -> int:
            randIndex = random.randint(0, r - l) + l
            nums[randIndex], nums[r] = nums[r], nums[randIndex]
            pivot = nums[r]

            nextSwapped = l
            for i in range(l, r):
                if nums[i] >= pivot:
                    nums[nextSwapped], nums[i] = nums[i], nums[nextSwapped]
                    nextSwapped += 1
            nums[nextSwapped], nums[r] = nums[r], nums[nextSwapped]

            count = nextSwapped - l + 1  # Number of nums >= pivot
            if count == k:
                return nums[nextSwapped]
            if count > k:
                return quickSelect(l, nextSwapped - 1, k)
            return quickSelect(nextSwapped + 1, r, k - count)

        return quickSelect(0, len(nums) - 1, k)
        
# @lc code=end

