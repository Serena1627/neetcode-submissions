# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return None
        node1 = l1
        node2 = l2
        dummy = ListNode(0)
        curr = dummy
        carry_over = 0
        while node1 or node2 or carry_over:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            total = val1 + val2 + carry_over
            carry_over = total // 10
            newVal = total % 10
            curr.next = ListNode(newVal)
            curr = curr.next

            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
        return dummy.next

        
        