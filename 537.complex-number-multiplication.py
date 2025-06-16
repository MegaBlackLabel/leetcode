#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        def parse_complex(num: str) -> tuple:
            real, imag = num[:-1].split('+')
            return int(real), int(imag)

        a, b = parse_complex(num1)
        c, d = parse_complex(num2)

        real_part = a * c - b * d
        imag_part = a * d + b * c

        return f"{real_part}+{imag_part}i"
# @lc code=end

