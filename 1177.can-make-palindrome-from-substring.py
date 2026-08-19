#
# @lc app=leetcode id=1177 lang=python3
#
# [1177] Can Make Palindrome from Substring
#

# @lc code=start
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [0] * (len(s) + 1)
        for i, char in enumerate(s):
            prefix[i + 1] = prefix[i] ^ (1 << (ord(char) - ord("a")))

        ans = []
        for left, right, k in queries:
            # XOR sum gives the combined parity of all characters in s[left...right]
            mask = prefix[right + 1] ^ prefix[left]
            # Count how many characters have an odd frequency
            odd_count = (mask).bit_count()
            # Each replacement (k) can fix up to 2 odd frequencies
            ans.append(odd_count // 2 <= k)

        return ans
# @lc code=end

