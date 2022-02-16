class Solution:
    def isHappy(self, n: int) -> bool:
        hset = set()
        
        while n not in hset:
            hset.add(n)
            if n == 1:
                return True
            else:
                n = self.sq_sum(n)
        else:
            return False
        
    def sq_sum(self, n):
        s = 0
        for i in str(n):
            s += int(i)**2
        return s
        
    
      