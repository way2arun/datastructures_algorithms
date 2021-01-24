"""
Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""

# Definition for singly-linked list.
import heapq
from typing import List


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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Solution 1 - 108 ms
        """
        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        return head.next
        """
        # Solution 2 -80 ms
        dummy = ListNode(0)
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next

        vals.sort()
        cur = dummy
        for val in vals:
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        return dummy.next


# Main Call
node1 = ListNode(1)
node1.next = ListNode(4)
node1.next.next = ListNode(5)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

node3 = ListNode(2)
node3.next = ListNode(6)

nodes_list = []
node_list = []

nodes_list.append(node1)
nodes_list.append(node2)
nodes_list.append(node3)

solution = Solution()
merge_node = solution.mergeKLists(nodes_list)
solution.printList(merge_node)
