# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root.left, root.right)
        
    def is_mirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        if t1.val == t2.val:
            outer = self.is_mirror(t1.left, t2.right)
            inner = self.is_mirror(t1.right, t2.left)
            return outer and inner
        else:
            return False
        
#         q = deque([root])
#         nxt_lvl = deque([])
        
#         while q:
#             for i in range(len(q)):
#                 item = q.popleft()
#                 if item.right:
#                     nxt_lvl.append(item.right)
#                     q.appendleft(item.right)
#                 if item.left:
#                     nxt_lvl.append(item.left)
#                     q.appendleft(item.left)
            
                
#             if len(nxt_lvl)%2 != 0:
#                 return False
                    
#             while nxt_lvl:
                
#                 left = nxt_lvl.popleft()
#                 right = nxt_lvl.pop()
                
#                 if left != right:
#                     return False
#         return True
            
                
            