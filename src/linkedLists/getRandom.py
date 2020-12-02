"""
Linked List Random Node
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
"""

# Definition for singly-linked list.
from random import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        # Solution 1 - 88 ms
        """
        self.head = head
        """
        # Solution 2 - 52 ms
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # Solution 1 - 88 ms
        """
        n, k = 1, 1
        head, ans = self.head, self.head
        while head.next:
            n += 1
            head = head.next
            if random() < k / n:
                ans = ans.next
                k += 1

        return ans.val
        """
        # Solution 2 - 52 ms
        pick = int(random() * len(self.range))
        return self.range[pick]


# Main Call
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

solution = Solution(head)
print(solution.getRandom())
