class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        l, r = 0, N-1
        
        
        while l <= r:
            m = (r+l)//2
            
            if nums[m] == target:
                return nums.index(target)
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        return -1
#         while nums[r+l//2] != target:
            
#             if target < nums[r+l//2]:
#                 r = r+l//2
#             elif target > nums[r+l//2]:
#                 l = r+l//2
#             elif target == nums[r+l//2]:
#                 return nums.index(target)
#         else:
#             return -1