from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l_n_z = 0  
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[l_n_z], nums[current] = nums[current], nums[l_n_z]
                l_n_z += 1