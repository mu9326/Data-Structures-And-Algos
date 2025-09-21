from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        # swap the two nodes (head and head.next)
        temp1, temp2 = head.next, head.next.next
        head.next = temp2
        temp1.next = head
        head = temp1

        # attach the rest of the recursive call on head.next.next to our curr list
        head.next.next = self.swapPairs(head.next.next)

        # return the new list
        return head


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Create list: 1 -> 2 -> 3 -> 4
head = build_linked_list([1, 2, 3, 4, 5, 6, 7])
print("Original list:")
print(head)

# Apply swapPairs
solution = Solution()
swapped = solution.swapPairs(head)
print("Swapped list:")
print(swapped)
