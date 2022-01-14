class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1 
        
        print(digits + [2])
        for i in range(n,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
        # for i in range(n):
        #     idx = n-i-1
        #     if(digits[idx] == 9):
        #         digits[idx] = 0
        #     else:
        #         digits[idx] += 1
        #         return digits
        # return [1] + digits
