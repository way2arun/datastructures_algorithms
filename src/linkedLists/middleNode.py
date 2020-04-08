"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

The number of nodes in the given list will be between 1 and 100.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Run time = 8ms
        if not head:
            return None

        curr = head
        count = 0
        index = {}
        while curr:
            index[count] = curr
            curr = curr.next
            count += 1

        mid = count // 2

        return index[mid]

        ("\n"
         "        # Runtime = 68ms \n"
         "        fast = slow = head\n"
         "        while fast and fast.next:\n"
         "            fast, slow = fast.next.next, slow.next\n"
         "        return slow\n"
         "        ")

    def print_nodes(self, node):
        node_list = []
        while node:
            print(node.val)
            node_list.append(node.val)
            node = node.next
        print(node_list)


# Main Call


# Load the linked list

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
middle_node = solution.middleNode(node1)
solution.print_nodes(middle_node)
