# Power Of Three


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        if n <= 0: return False
        x, i = 1, 0

        while x <= n:
            if x == n: return True
            i += 1
            x = n ** i

        return False
'''
        mx = n**19

        return n>0 and mx%n ==0
