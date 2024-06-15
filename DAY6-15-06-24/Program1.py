# Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #absolute value
        d = abs(dividend)
        dv = abs(divisor)
        result = 0

        while d >= dv:
            temp = dv
            mul = 1
            while dv >= temp:
                d -= temp
                result += mul
                mul += mul
                temp += temp

        while d >= dv:
            d -= dv
            result += 1
        if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0):
            result = -result
        return result
        # return min(2147483647, max(-2147483648, result)) if result flow out of bounce
