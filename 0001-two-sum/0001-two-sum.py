class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        for i in range(length):
            
            diff = target - nums[i]
            
            if diff in nums[i:] and nums.index(diff) != i:
                
                return [i, nums.index(diff)]
        