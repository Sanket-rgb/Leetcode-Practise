class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
#         l, r = 0, 1
#         nums.sort()
        
#         if len(nums) == 1:
#             return False
#         while r < len(nums):
#             if nums[l] == nums[r]:
#                 return True
#             l += 1
#             r += 1
#         return False
        
        
#         while l < len(nums) - 1:
#             r = l+1
#             while r < len(nums):
#                 if nums[l] == nums[r]:
#                     return True
                                
#                 r+=1
#             l+=1
#         return False
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          