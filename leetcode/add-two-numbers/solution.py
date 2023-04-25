from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        result = None
        t = None
        carry = 0
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next

            val += carry
            carry = val // 10
            val = val % 10

            if result is None:
                result = ListNode(val)
                t = result
            else:
                new = ListNode(val)
                t.next = new
                t = t.next

        if carry:
            new = ListNode(carry)
            t.next = new
            t = t.next

        return result
