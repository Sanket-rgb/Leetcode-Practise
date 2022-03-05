# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        depth = 0
        
        while q:
            for i in range(len(q)):
                item = q.popleft()
                if item.right:
                    q.append(item.right)
                if item.left:
                    q.append(item.left)
                
                
            depth += 1
        return depth
#         if not root:
#             return 0
        
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
#         if root == None:
#             return 0
        
#         depth = 0
#         q = deque([root])
        
#         while q:
#             for i in range(len(q)):
#                 item = q.popleft()
#                 if item.left:
#                     q.append(item.left)
#                 if item.right:
#                     q.append(item.right)
#             depth += 1
#         return depth
                
        