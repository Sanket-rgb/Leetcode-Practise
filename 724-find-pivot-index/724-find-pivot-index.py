class Solution:
    def get_leftaddition(self, arr, index):
        left_sum = 0
        
        for i in range(index):
            left_sum += arr[i]
        return left_sum
    
    def get_rightaddition(self, arr, index):
        right_sum = 0
        length = len(arr) - 1
        
        for i in range(length, index, -1):
            right_sum += arr[i]
        return right_sum
            
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        s= sum(nums)
        
        if length == 1:
            return 0
        left_sum = 0
        
        while i < length:
            
            right_sum = s - nums[i] - left_sum
                
            if left_sum == right_sum:
                return i 
#             left_sum = self.get_leftaddition(nums, i)
#             right_sum = self.get_rightaddition(nums, i)
                
#             if left_sum == right_sum:
#                 return i 
#             if i == 0:
#                 left_sum = 0
#                 right_sum = self.get_rightaddition(nums, i)
                
#                 if left_sum == right_sum:
#                     return 0
#             elif i == length-1:
#                 left_sum = self.get_leftaddition(nums, i)
#                 right_sum = 0
                
#                 if left_sum == right_sum:
#                     return i
#             else:
#                 left_sum = self.get_leftaddition(nums, i)
#                 right_sum = self.get_rightaddition(nums, i)
                
#                 if left_sum == right_sum:
#                     return i 
            left_sum += nums[i]
            i += 1
        return -1