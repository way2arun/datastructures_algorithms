"""
Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
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
            print(node.val)
            node_list.append(node.val)
            node = node.next
        print(node_list)

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Solution 1 - 44 ms
        """
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        cur = head
        prev = dummy

        dup = 0

        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                cur = cur.next
                dup = 1
            else:
                if dup == 1:
                    prev.next = cur.next
                    cur = cur.next
                    dup = 0
                else:
                    prev = cur
                    cur = cur.next
        if dup == 1:
            prev.next = cur.next
            cur = cur.next

        return dummy.next
        """
        # Solution 2 - 20 ms
        prev = head
        tmp = head
        s = set()
        while tmp:
            found_duplicate = False
            while tmp and tmp.next and tmp.val == tmp.next.val:
                found_duplicate = True
                tmp = tmp.next
            if found_duplicate:
                if head.val == tmp.val and tmp.next is None:
                    print("la")
                    return None
                if tmp.val == head.val:
                    if tmp.next is None:
                        prev.next = None
                        return head
                    head = tmp.next
                    prev = head
                    continue

                if head.val == tmp.val and tmp.next is None:
                    return None
                prev.next = tmp.next
                tmp = prev
                continue
            prev = tmp
            tmp = tmp.next

        return head


# Main Call

head = ListNode(val=1)
head.next = ListNode(val=1)
head.next.next = ListNode(val=1)
head.next.next.next = ListNode(val=2)
head.next.next.next.next = ListNode(val=3)

solution = Solution()
node = solution.deleteDuplicates(head)
solution.print_nodes(node)
