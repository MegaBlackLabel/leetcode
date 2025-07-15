#
# @lc app=leetcode id=640 lang=python3
#
# [640] Solve the Equation
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        
        left, right = equation.split('=')
        def parse(s):
            s = s.replace('-', '+-')
            terms = s.split('+')
            x_count, num_count = 0, 0
            for term in terms:
                if 'x' in term:
                    if term == 'x':
                        x_count += 1
                    elif term == '-x':
                        x_count -= 1
                    else:
                        x_count += int(term[:-1])
                elif term:
                    num_count += int(term)
            return x_count, num_count
        
        left_x, left_num = parse(left)
        right_x, right_num = parse(right)
        
        total_x = left_x - right_x
        total_num = right_num - left_num
        
        if total_x == 0:
            return "No solution" if total_num != 0 else "Infinite solutions"
        
        return f"x={total_num // total_x}"
# @lc code=end

