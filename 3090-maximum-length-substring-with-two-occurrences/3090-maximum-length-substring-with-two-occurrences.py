from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = Counter()
        l = 0
        best = 0

        for r, ch in enumerate(s):
            freq[ch] += 1

            
            while freq[ch] > 2:
                freq[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best
