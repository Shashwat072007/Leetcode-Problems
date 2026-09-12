

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                # mid is higher than the picked number
                right = mid - 1
            else:
                # mid is lower than the picked number
                left = mid + 1
