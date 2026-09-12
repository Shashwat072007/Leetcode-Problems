class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        w=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[w]=nums[i]
                w+=1
        return w    
        