class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        res = []
        
        while i < j:
            s = numbers[i] + numbers[j]
            
            if s == target:
                return [i+1, j+1]
            elif s < target:
                i += 1
            else:
                j -= 1
        return -1
#         length = len(numbers)
#         res = []
        
#         for i in range(length):
#             for j in range(1, length):
#                 s = numbers[i] + numbers[j]
                
#                 if i == j:
#                     pass
#                 elif s == target:
#                     index1 = numbers.index(numbers[i]) + 1
#                     if numbers[i] == numbers[j]:
#                         index2 = numbers.index(numbers[j]) + 2
#                     else:
#                         index2 = numbers.index(numbers[j]) + 1
#                     res.append(index1)
#                     res.append(index2)
                    
#                     return res
        