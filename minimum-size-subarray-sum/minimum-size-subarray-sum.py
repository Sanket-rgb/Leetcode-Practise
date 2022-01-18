class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = sys.maxsize
        left = 0
        val_sum = 0
        
        for i in range(len(nums)):
            val_sum += nums[i]
            
            while val_sum >= target:
                result = min(result, i+1-left)
                val_sum -= nums[left]
                left += 1
        return result if result != sys.maxsize else 0
        
        
                