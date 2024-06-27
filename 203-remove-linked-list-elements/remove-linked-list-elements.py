# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        while head and head.val==val:
            nextt=head.next
            head.next=None
            head=nextt
        dummy=head
        prev=None
        while dummy and dummy.next:
            nextt=dummy.next.next
            prev=dummy
            dummy=dummy.next
            while dummy and dummy.val==val:
                prev.next=nextt
                dummy.next=None
                dummy=nextt
                if nextt:
                    nextt=nextt.next
                else:
                    nextt=None
        if prev and prev.val==val:
            return None
        return head
