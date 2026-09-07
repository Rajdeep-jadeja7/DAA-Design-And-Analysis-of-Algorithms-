# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        length=0
        k=0
        while curr!=None and curr.next!=None:
            curr=curr.next
            length+=1
        if (length==0 and n==1):
            return None

        k=length - n+1
        if length+1 == n:
            head=head.next
            return head
        curr = head 
        for i in range(k-1):
            curr = curr.next
        if curr.next!=None:
            curr.next = curr.next.next   
        return head     


        