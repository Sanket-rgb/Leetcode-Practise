class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        N = len(nums)
        hashmap = {}
        
        for i in range(N):
            hashmap[nums[i]] = i
        
        for i in range(N):
            c = target - nums[i]
            
            if c in hashmap and hashmap[c] != i:
                return [i, hashmap[c]]
        # for i in range(N):
        #     for j in range(i+1, N):
        #         if nums[j] == target - nums[i]:
        #             return [i, j]
        
        
#         for i in nums:
#             c = target - i
            
#             if c in nums and c!=i:
#                 return [nums.index(i), nums.index(c)]