# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        visited = []
        output = []
        curr = root
        
        # if curr.left is None:
        #         output.append(curr.val)
        #         curr = stack.pop()
        #         output.append(curr.val)
        #         curr = curr.right
        #         stack.append(curr)
        
        while curr is not None or stack:
            
            while curr is not None:
                stack.append(curr)
                curr = curr.left
                
            # output.append(stack.pop())
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        return output
        
            
            
        