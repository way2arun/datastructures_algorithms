"""
Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Solution 1 - 48 ms
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: break

        if not fast or not fast.next: return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        """
        # Solution 2 - 24 ms
        visited = set()
        tail = head
        while tail:
            if tail.next in visited:
                return tail.next
            visited.add(tail)
            tail = tail.next
        return None


# Main Call
head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

pos = node1
solution = Solution()
node = solution.detectCycle(head)
if node == pos:
    print("connected")
