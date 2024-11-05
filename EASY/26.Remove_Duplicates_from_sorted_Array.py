class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        zero_index = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[zero_index]:
                zero_index += 1
                nums[zero_index] = nums[i]
                
        return zero_index + 1
        
