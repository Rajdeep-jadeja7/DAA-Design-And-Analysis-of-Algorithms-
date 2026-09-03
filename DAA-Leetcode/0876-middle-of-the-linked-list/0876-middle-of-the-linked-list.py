# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        count=1

        curr=head

        while (curr!=None and curr.next!=None):
            count+=1
            curr=curr.next

        mid = count//2
        curr=head
        for i in range(mid+1):
            if i == mid:
                head=curr
            else:    
                curr=curr.next
        return head        

        