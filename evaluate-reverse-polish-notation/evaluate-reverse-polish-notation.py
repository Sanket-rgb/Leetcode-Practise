class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # num = int(tokens[0])+int(tokens[1])
        
        # for item in tokens:
        #     print(item)
        
        stack = []
        
        for item in tokens:
            if item != "+" and item != "-" and item != "/" and item != "*":
                stack.append(int(item))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                
                if item == "+":
                    stack.append(num1 + num2)
                if item == "-":
                    stack.append(num2 - num1)
                if item == "/":
                    stack.append(int(num2 / num1))
                if item == "*":
                    stack.append(num1 * num2)
        return stack.pop()