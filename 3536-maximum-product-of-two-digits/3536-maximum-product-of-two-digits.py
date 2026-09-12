class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        digits.sort()
        last_two = digits[-2:]
        return last_two[0] * last_two[1]