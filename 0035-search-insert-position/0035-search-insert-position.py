class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start = 0
        end = length - 1
        
        
            
        while start <= end:
            midpoint = (start + end) // 2
            
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                start = midpoint + 1
            elif nums[midpoint] > target:
                end = midpoint - 1
            
        return start
        