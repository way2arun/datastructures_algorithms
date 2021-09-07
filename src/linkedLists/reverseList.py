"""
Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printList(self, node):
        temp = node
        while (temp):
            print(temp.val)
            temp = temp.next

    def reverseList(self, head: ListNode) -> ListNode:
        # Solution 1 - 28 ms
        """
        curr = None
        nxt = head
        while nxt:
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp

        return curr
        """
        # Solution 2 - 12 ms
        if head is None:
            return None

        previousNode = None
        currentNode = head

        while True:
            # Swap the direction of the next pointer to point to the previous
            nextNode = currentNode.next
            currentNode.next = previousNode

            # Move onto the next
            if nextNode is None:
                break

            previousNode = currentNode
            currentNode = nextNode

        return currentNode


# Main Call
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
node = solution.reverseList(head)
solution.printList(node)
