class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        
        while start <= end:
            while start < end and not self.alphaNum(s[start]):
                start += 1
            while end > start and not self.alphaNum(s[end]):
                end -= 1
            
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        return True
                
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))    
        
        
        
#         newS = s.lower()
#         ss = ""
#         for item in ss:
#             if ord(item) >= 97 or ord(item) <= 122:
#                 ss += item
                   
#         start = 0
#         end = len(ss) - 1
        
        
#         while start <= end:
#             if ss[start] != ss[end]:
#                 return False
            
#             start += 1
#             end -= 1
#         return True