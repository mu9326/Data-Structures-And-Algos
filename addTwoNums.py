# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import Optional

# 17 // 10 = 1
# 17 % 10 = 7

# 2 --> 4 --> 3 --> None
# 5 --> 6 --> None


# carry = 0, total = 0
# dummy --> 7 --> 0 (t) --> 4 (t) --> None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = tail = ListNode()
        carry = 0

        while l1 or l2 or carry:
            total = carry  # start with carry each loop
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next

        return dummy.next
