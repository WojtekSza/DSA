# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy=head
        prev=None
        duplicates=defaultdict(int)
        while dummy:
            duplicates[dummy.val]+=1
            dummy=dummy.next
        dummy=head
        while dummy and dummy.next:
            prev=dummy
            nextt=dummy.next.next
            dummy=dummy.next
            while dummy and duplicates[dummy.val]>1 :
                prev.next=nextt
                dummy.next=None
                dummy=nextt
                if nextt:
                    nextt=nextt.next
                else:
                    nextt=None
        if duplicates[head.val]>1:
            nextt=head.next
            head.next=None
            head=nextt
        return head