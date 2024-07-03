# Factorial Trailing Zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        oc = 5
        count = 0
        while (n/oc >= 1):
            count += n//oc
            oc = oc*5
        return count
