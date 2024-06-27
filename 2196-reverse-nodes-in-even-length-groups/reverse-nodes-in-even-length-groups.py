# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data=[]
        sub_data=[]
        dummy=head
        g=1
        while dummy:
            sub_data.append(dummy.val)
            if len(sub_data)==g:
                data.append(sub_data)
                sub_data=[]
                g+=1
            dummy=dummy.next
        if len(sub_data)!=0:
            data.append(sub_data)
        for i in range(len(data)):
            if len(data[i])%2==0:
                reverse=[]
                for j in range(1,len(data[i])+1):
                    reverse.append(data[i][-j])
                data[i]=reverse
        data=[item for row in data for item in row]
        data
        curr=head
        lenght=0
        while curr:
            curr.val=data[lenght]
            lenght+=1
            curr=curr.next
        return head
        