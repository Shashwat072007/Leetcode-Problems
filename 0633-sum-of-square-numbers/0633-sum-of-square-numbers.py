class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = isqrt(c)
        while l <= r:
            t = l**2 + r**2
            if t == c:
                return True
            elif t < c:
                l += 1
            else:
                r -= 1
        return False 