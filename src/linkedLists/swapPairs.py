"""
Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_nodes(self, node):
        node_list = []
        while node:
            node_list.append(node.val)
            node = node.next
        print(node_list)

    def swapPairsHelper(self, curHead) -> None:
        if not curHead or not curHead.next:
            return
        curHead.val, curHead.next.val = curHead.next.val, curHead.val
        self.swapPairsHelper(curHead.next.next)

    def swapPairs(self, head: ListNode) -> ListNode:
        # Solution 1 - 28 ms
        """
        if not head or not head.next:
            return head
        tmp = head
        head = head.next
        tmp.next = head.next
        head.next = tmp
        tmp.next = self.swapPairs(tmp.next)
        return head
       """
        # Solution 2 - 8 ms
        self.swapPairsHelper(head)
        return head


# Main Call
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

solution = Solution()
swap = solution.swapPairs(head)
solution.print_nodes(swap)
