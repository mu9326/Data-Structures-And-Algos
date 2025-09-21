from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # we have the heads of two lists
        # initialize a dummy node
        dummy = ListNode()
        curr = dummy
        head1, head2 = list1, list2

        while head1 or head2:
            if not head1 and head2:
                curr.next = head2
                break

            if not head2 and head1:
                curr.next = head1
                break

            if head1.val <= head2.val:
                temp = head1.next
                curr.next = head1
                head1.next = None
                head1 = temp
                curr = curr.next

            else:
                temp = head2.next
                curr.next = head2
                head2.next = None
                head2 = temp
                curr = curr.next

        return dummy.next
