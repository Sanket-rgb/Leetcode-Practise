class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        
        while i < len(s):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif not stack:
                return False
            elif s[i] == ")":
                if stack.pop() != "(":
                    return False
            elif s[i] == "]":
                if stack.pop() != "[":
                    return False
            elif s[i] == "}":
                if stack.pop() != "{":
                    return False
                         
            i += 1
        
        if stack:
            return False
        else:
            return True