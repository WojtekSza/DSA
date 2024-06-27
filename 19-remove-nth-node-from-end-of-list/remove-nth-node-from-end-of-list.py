# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy=head
        step=lenght=0
        prev=None
        while dummy:
            dummy=dummy.next
            lenght+=1
        if lenght==1:
            return None
        end=lenght-n
        dummy=head
        while dummy and dummy.next:
            prev=dummy
            nextt=dummy.next.next
            dummy=dummy.next
            if step==end and end==0:
                head=dummy
            step+=1
            if step==end and end!=0:
                prev.next=nextt
                dummy.next=None
        return head