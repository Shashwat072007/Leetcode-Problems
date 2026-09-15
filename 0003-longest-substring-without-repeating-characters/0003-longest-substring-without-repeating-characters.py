class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c=set()
        l=0
        lo=0
        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l+=1
            c.add(s[r])
            lo=max(lo,r-l+1)
        return lo