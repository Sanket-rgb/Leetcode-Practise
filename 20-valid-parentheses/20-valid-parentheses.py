class Solution(object):
    def isValid(self, s):
        stack = []
        
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack.pop() != item:
                return False
        if len(stack) != 0:
            return False
        else:
            return True
            
                
                
                
                
                
                
        
        
        
        
        
        
        
        # stack = []
        # for item in s:
        #     if item == '(':
        #         stack.append(")")
        #     elif item == "[":
        #         stack.append("]")
        #     elif item == "{":
        #         stack.append("}")   
        #     elif not stack or stack.pop() != item:
        #         return False
        # return not len(stack)
        