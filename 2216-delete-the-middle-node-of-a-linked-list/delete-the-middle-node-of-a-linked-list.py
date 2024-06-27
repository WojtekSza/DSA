# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy=head
        lenght=0
        while dummy:
            dummy=dummy.next
            lenght+=1
        if lenght==1:
            return None
        mid=lenght//2
        dummy=head
        step=0
        while dummy and dummy.next:
            prev=dummy
            nextt=dummy.next.next
            dummy=dummy.next
            step+=1
            if step==mid:
                dummy.next=None
                prev.next=nextt
        return head