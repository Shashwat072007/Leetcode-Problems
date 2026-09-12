class Solution:
    def plusOne(self, digits):
        i = len(digits) - 1
        digits[i] += 1

        # handle carry
        while i > 0 and digits[i] == 10:
            digits[i] = 0
            i -= 1
            digits[i] += 1

        # if overflow at the front, insert 1
        if digits[0] == 10:
            digits[0] = 1
            digits.insert(1, 0)

        return digits
