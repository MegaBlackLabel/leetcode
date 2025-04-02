#
# @lc app=leetcode id=385 lang=python3
#
# [385] Mini Parser
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#         if value is None:
#             self.value = []
#         else:
#             self.value = value

#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#        return isinstance(self.value, int)

#    def add(self, elem):
#         if not isinstance(self.value, list):
#             self.value = []
#         self.value.append(elem)

#    def setInteger(self, value):
#         self.value = value

#    def getInteger(self):
#        if self.isInteger():
#            return self.value
#        return None

#    def getList(self):
#         if not self.isInteger():
#                 return self.value
#         return None

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []

        for i, c in enumerate(s):
            if c == '[':
                stack.append(NestedInteger())
                start = i + 1
            elif c == ',':
                if i > start:
                    num = int(s[start:i])
                    stack[-1].add(NestedInteger(num))
                start = i + 1
            elif c == ']':
                popped = stack.pop()
                if i > start:
                    num = int(s[start:i])
                    popped.add(NestedInteger(num))
                if stack:
                    stack[-1].add(popped)
                else:
                    return popped
                start = i + 1
# @lc code=end

