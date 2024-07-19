# sum of Two Integer

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # solution 1
        # return sum([a,b])

        # solution 2
        while b > 0:
            a, b = a^b, (a&b) << 1 # ((a&b) << 1) is bit shifting left by 1
        return a
