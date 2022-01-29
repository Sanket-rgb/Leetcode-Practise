class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        N = len(s)
        count = 1
        stack = []
        
        if N == 1: return False
        
        for item in s:
            if item == "(":
                stack.append(")")
            elif item == "[":
                stack.append("]")
            elif item == "{":
                stack.append("}")
            elif len(stack) == 0 or stack.pop() != item:
                return False
        return not len(stack)
    # True if len(stack) == 0 else False
#         for item in s:
            
#             if item == "(" or item == "[" or item == "{":
#                 stack.append(item)
#             elif item == ")" or item == "]" or item == "}":
#                 if len(stack) == 0: return False
#                 if stack.pop() != dic[item]:
#                     return False
#             count += 1
#         return False if len(stack) != 0 else True
    
    
        