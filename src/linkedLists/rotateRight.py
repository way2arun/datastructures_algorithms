"""
Rotate List
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Solution 1 - 36 ms
        """
        if not head or not head.next:
            return head
        last, n = head, 1
        while last.next:
            last = last.next
            n += 1

        if k % n == 0: return head

        middle = head
        for i in range(n - k % n - 1):
            middle = middle.next

        new_head = middle.next
        last.next = head
        middle.next = None
        return new_head
        """
        # Solution 2 - 20 ms
        if not head:
            return None

        length, oldTail = self.size(head)
        k = k % length
        if k == 0:
            return head
            # print('k:',k)
        prev = None
        curr = head
        i = k
        first = head
        while i and first:
            first = first.next
            i -= 1
        # print('first:',first)
        second = head
        newTail = None
        while first:
            newTail = second
            second = second.next
            first = first.next
        # print('newTail:',newTail)
        # print('second:',second)
        newTail.next = None
        # print('head:',head)
        # print('prev:',prev)
        # print('curr:',curr)
        # print('tail:',tail)
        if oldTail:
            oldTail.next = head
        # print(second)
        return second

    def size(self, head):
        length = 0
        tail = None
        while head:
            tail = head
            head = head.next
            length += 1
        return length, tail

    def print_nodes(self, node):
        node_list = []
        while node:
            print(node.val)
            node_list.append(node.val)
            node = node.next
        print(node_list)


# Main Call
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
k = 2
new_node = solution.rotateRight(node1, k)
solution.print_nodes(new_node)
