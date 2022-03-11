# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root,targetSum - root.val)]
        
        
        
        while stack:
            node, remainingSum = stack.pop()
            if not node.left and not node.right and remainingSum == 0:
                return True
            if node.right:
                stack.append((node.right, remainingSum - node.right.val))
            if node.left:
                stack.append((node.left, remainingSum - node.left.val))
        return False
                
                