# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            nextPair = curr.next.next
            second = curr.next
            
            second.next = curr
            curr.next = nextPair
            prev.next = second
            
            prev = curr
            curr = nextPair
        return dummy.next
            
#         if head is None:
#             return
        
        
#         curr = head
#         while curr.next is not None:
#             curr.next = curr.next.next
#             curr.next.next = curr
#             if curr.next is not None:
#                 curr = curr.next
#         return head
        # while curr.next is not None:
        #     curr.val, curr.next.val = curr.next.val, curr.val
        #     if curr.next.next is not None:
        #         curr = curr.next.next
        # return head
        # if head.next.next:
        #     head.val, head.next.val = head.next.val, head.val
        #     head = head.next.next
        #     self.swapPairs(head)