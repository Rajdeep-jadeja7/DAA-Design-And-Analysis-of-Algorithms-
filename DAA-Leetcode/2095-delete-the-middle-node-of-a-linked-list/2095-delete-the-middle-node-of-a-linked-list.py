# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        l=1
        while(curr.next!=None):
            l+=1
            curr=curr.next
        if l==1:
            return None
        mid=(l//2)   
        curr = head
       
        for i in range(mid-1):
            curr = curr.next 
        if curr.next!=None:    
            curr.next=curr.next.next
        
        return head    

