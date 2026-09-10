# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if headA==None or headB==None:
            return None
        if headA.next==None and headB.next==None:
            if headA==headB:
                return headA    
        curr1=headA
        curr2=headB

        l1=1
        l2=1
        while(curr1!=None and curr1.next!=None):
            curr1=curr1.next
            l1+=1

        while(curr2!=None and curr2.next!=None):
            curr2=curr2.next
            l2+=1 
        
        if(l1>l2):
            l1=l1-l2
            for i in range(l1):
                headA=headA.next

        elif(l2>l1):
            l2=l2-l1
            for i in range(l2):
                headB=headB.next

        if(l1==1 and l2==1):
            if headA==headB:
                return headA
            else:
                return None     

        while(headA!=None or headB!=None):
                if headA==headB:
                    return headA
                else:
                    headA=headA.next
                    headB=headB.next   
        return None              
        




        