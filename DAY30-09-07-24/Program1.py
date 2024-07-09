# Basic Calculator II

class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, "+", []
        for i in s+"+":
            if i.isdigit():
                num = num*10 + int(i)
            elif i in "+-*/":
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop()*num)
                if sign == "/":
                    stack.append(math.trunc(stack.pop()/num))
                sign = i
                num = 0
        return sum(stack)
