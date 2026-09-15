class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=len(s)
        for i in range(l):
            u=True
            for j in range(l):
                if i!=j and s[i]==s[j]:
                    u=False
                    break
            if u:
                return i
        return -1