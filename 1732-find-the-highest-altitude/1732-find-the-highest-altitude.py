class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude=[]
        altitude.append(0)
        s=0
        for i in gain:
            s+=i
            altitude.append(s)
        return max(altitude)