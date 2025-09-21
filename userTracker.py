# Question -
# Write a userTracker program that performs the following functions.
# recordVisit(self, username) records each visit by a certain user.
# getFirstVisitOnce(self) gets the first visit of the user who has visited exactly once.
# For example -
# tracker = UserTracker()
# tracker.recordVisit("Alice")
# tracker.recordVisit("Bob")
# tracker.recordVisit("Alice")
# tracker.recordVisit("Charlie")
# tracker.getFirstVisitOnce() --> returns "Bob" (note: the returned answer has to be in order because Bob visited first)

# My answer -
# class ListNode:
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next


# class UserTracker:
#     def __init__(self):
#         self.records = set()
#         self.head = self.tail = ListNode("")

#     def recordVisit(self, username):
#         # use a hashset
#         # if the element is already in the hashset:
#         if username in self.records:
#             # remove it from the linked list
#             prev = self.head
#             curr = self.head.next
#             while curr:
#                 if curr.val == username:
#                     # temp = curr.next
#                     prev.next = curr.next
#                     break
#                 prev = curr
#                 curr = curr.next

#         else:
#             # add it to the hashset
#             self.records.add(username)
#             # add it to the linked list
#             self.tail.next = ListNode(username)
#             self.tail = self.tail.next
#         pass

#     def getFirstVisitOnce(self):
#         # return the first element of the linked list
#         return self.head.next


# the above approach does not keep track of the number of times a user has visited the website
# use a hashmap for that
# also, prev node references can be stored in the hashmap, so that they can be deleted in O(1) time


class ListNode:
    def __init__(self, val, next=None):
        self.val = val  # store the username
        self.next = next  # pointer to the next node


class UserTracker:
    def __init__(self):
        self.counts = {}  # hashmap: username -> number of visits
        self.head = self.tail = ListNode(
            ""
        )  # dummy head node (makes list operations easier)
        self.node_map = {}  # hashmap: username -> previous node (for O(1) deletion in linked list)

    def recordVisit(self, username):
        if username not in self.counts:
            # Case 1: First visit
            self.counts[username] = 1

            # Create a new node for this user and add to the end of the linked list
            new_node = ListNode(username)
            self.tail.next = new_node
            self.node_map[username] = (
                self.tail
            )  # store previous node for quick deletion later
            self.tail = new_node  # update tail pointer
        else:
            # Case 2: User has visited before
            self.counts[username] += 1

            # If this is their second visit, remove them from the linked list
            if self.counts[username] == 2:
                prev = self.node_map[username]  # get previous node in the list
                curr = prev.next  # current node (the one to remove)

                # unlink current node
                prev.next = curr.next

                # if the removed node was the tail, update tail pointer
                if curr == self.tail:
                    self.tail = prev

                # remove user from node_map (they're no longer in the list)
                del self.node_map[username]

                # if there's a next node, update its mapping to point to the new prev
                if curr.next:
                    self.node_map[curr.next.val] = prev

    def getFirstVisitOnce(self):
        # return the first node in the linked list (if exists),
        # otherwise return None
        if self.head.next:
            return self.head.next.val
        return None


# An alternate approach would be to use a heap to store ALL the entries, not just the one -
# (1, "Alice")
# (2, "Bob")
# (3, "Alice")
# (4, "Charlie")

# Key point

# You don’t need the "duplicate user" to be at the root in order to eventually discard it.
# Because:
# The heap always pops the smallest timestamp first.
# If an early user (say "Alice") is invalid because they’ve visited twice, eventually their earliest entry will reach the root (since no smaller timestamp exists).
# Once you pop it, the later duplicate (e.g. (3, "Alice")) will also eventually bubble up to the root when its turn comes.
# You’ll discard all invalid entries one by one until you reach the first valid single-visit user.
