# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ref=[]
        dummy=head
        while dummy:
            ref.append(dummy.val)
            dummy=dummy.next
        prev=None
        curr=head
        while curr:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        check=[]
        while prev:
            check.append(prev.val)
            prev=prev.next
        return ref==check

        