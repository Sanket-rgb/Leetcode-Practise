# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         queue = [root], next_level = [], current_level = [], result = []

        
        if root is None:
            return []
        
        queue = [root]
        next_level = []
        current_level = []
        output = []
        
        while queue != []:
            for item in queue:
                current_level.append(item.val)
                if item.left is not None:
                    next_level.append(item.left)
                if item.right is not None:
                    next_level.append(item.right)
            output.append(current_level)
            current_level = []
            queue = next_level
            next_level = []
            
        return output
        
        
        
        