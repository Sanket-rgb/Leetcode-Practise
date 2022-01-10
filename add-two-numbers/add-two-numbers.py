# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = dummy = ListNode(0)
        carry = 0
        p = l1
        q = l2
        
        while p != None or q != None:
            x = p.val if p else 0
            y = q.val if q else 0
            
            summation = x + y + carry
            
            carry = summation // 10
            
            curr.next = ListNode(summation % 10)
            curr = curr.next
            
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next
        
        
#         while l1 != None and l2 != None:
#             if carry:
#                 num = ListNode(l1.val + l2.val + 1)
#             else:
#                 num = ListNode(l1.val + l2.val)
            
#             if num.val > 9:
#                 rem = num.val % 10
#                 curr.next = rem
#                 curr = curr.next
#                 carry = True
#             else:
                
#                 curr.next = num
#                 curr = curr.next
#                 carry = False
            
#             l1 = l1.next
#             l2 = l2.next
            
#         curr.next = l1 or l2
            
#         return dummy.next
                
                
                
                