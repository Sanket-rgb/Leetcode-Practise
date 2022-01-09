# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self, head):
        count = 0
        while head:
            count+=1
            head = head.next
            
        return count
    
    def get_end_of_firsthalf(self, head):
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def second_half_start(self, head):
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        first_half_end = self.get_end_of_firsthalf(head)
        second_half_start = self.second_half_start(first_half_end.next)
        
        first_position = head
        second_position = second_half_start
        
        while second_position:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next
        return True
            
            
            
        
        
        
        
#         while i < length//2:
            
#             for j in range(ll-1):
#                 end = end.next
#             print(start.val, end.val)
#             if start.val == end.val:
                
#                 end = head
#             else:
#                 return False
#             # start = start.next
#             ll -= 1
#             i += 1
#             start = start.next
#         return True
            
        # while length//2 > 0:
        #     for i in range(length):
        #         end = end.next
        #     if start == end:
        #         start = start.next
        #         length-=1
        #     else:
        #         return False
        #     length-=1
        # return True
        
        