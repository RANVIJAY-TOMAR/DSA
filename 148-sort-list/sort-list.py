# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        List = []
        temp = head

        
        while temp:
            List.append(temp.val)
            temp = temp.next

       
        List.sort()

        
        temp = head
        for val in List:
            temp.val = val
            temp = temp.next

        return head


        
        
        