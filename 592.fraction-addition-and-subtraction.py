#
# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#

# @lc code=start
class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)

        def add_fractions(frac1, frac2):
            num1, den1 = frac1
            num2, den2 = frac2
            common_den = lcm(den1, den2)
            new_num = (num1 * (common_den // den1)) + (num2 * (common_den // den2))
            common_gcd = gcd(new_num, common_den)
            return (new_num // common_gcd, common_den // common_gcd)

        fractions = []
        i = 0
        n = len(expression)
        sign = 1

        while i < n:
            if expression[i] in '+-':
                sign = -1 if expression[i] == '-' else 1
                i += 1
            
            j = i
            while j < n and expression[j] not in '+-':
                j += 1
            
            num, den = map(int, expression[i:j].split('/'))
            fractions.append((sign * num, den))
            i = j
        
        result_fraction = (0, 1)
        for frac in fractions:
            result_fraction = add_fractions(result_fraction, frac)

        return f"{result_fraction[0]}/{result_fraction[1]}"
# @lc code=end

