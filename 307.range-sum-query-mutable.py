#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.add(i, nums[i])

    def update(self, index: int, val: int) -> None:
        self.add(index, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.sum(right) - self.sum(left - 1)

    def add(self, index: int, val: int) -> None:
        index += 1
        while index < len(self.bit):
            self.bit[index] += val
            index += index & -index

    def sum(self, index: int) -> int:
        index += 1
        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

