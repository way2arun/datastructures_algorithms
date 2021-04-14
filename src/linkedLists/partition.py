"""
Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printList(self, head):
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next

    def partition(self, head: ListNode, x: int) -> ListNode:
        # Solution 1 - 36 ms
        """
        d1 = ListNode(-1)
        d2 = ListNode(-1)
        p1, p2 = d1, d2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next

        p1.next = d2.next
        p2.next = None
        return d1.next
        """
        # Solution 2 - 16 ms
        if head is None:
            return None
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        e1, e2 = dummy1, dummy2
        while head:
            if head.val < x:
                e1.next = head
                e1 = e1.next
            else:
                e2.next = head
                e2 = e2.next
            head = head.next

        e2.next = None  # e2 will be atleast dummy, hence no need to check whether e2 exists or not
        e1.next = dummy2.next

        return dummy1.next


# Main Call
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
x = 3
solution = Solution()
node = solution.partition(head, x)
solution.printList(node)
