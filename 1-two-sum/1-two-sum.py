class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        N = len(nums)
        hashmap = {}
        
        for i,item in enumerate(nums):
            hashmap[item] = i
        for i in nums:
            c = target - i
            if c in hashmap and hashmap[c] != nums.index(i):
                return [hashmap[c], nums.index(i)]
        
#         for i in nums:
#             c = target - i
            
#             if c in nums and c!=i:
#                 return [nums.index(i), nums.index(c)]