# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head
        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next.next if temp.next else None
        temp = head.next
        while temp:
            values.append(temp.val)
            temp = temp.next.next if temp.next else None
        temp = head
        i = 0
        while temp!= None:
            temp.val = values[i]
            i+= 1
            temp = temp.next
        return head