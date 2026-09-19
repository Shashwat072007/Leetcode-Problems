class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        x=sorted(set(nums),reverse=True)
        if len(x)>=3:
            return x[2]
        return x[0]