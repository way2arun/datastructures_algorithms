"""
Split Linked List in Parts
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.



Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.


Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
   Hide Hint #1
If there are N nodes in the list, and k parts, then every part has N/k elements, except the first N%k parts have an extra one.
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def find(self, head, n):
        prev = None
        for i in range(n):
            prev = head
            if head == None:
                return None
            head = head.next
        if prev is not None:
            prev.next = None
        return head

    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        # Solution 1 - 36 ms
        """
        def getLength(head):
            cnt = 0
            while head is not None:
                cnt += 1
                head = head.next
            return cnt

        listSize = getLength(head)
        partSize, remainSize = listSize // k, listSize % k
        ans = []
        while head is not None:
            curPartSize = partSize
            if remainSize > 0:
                remainSize -= 1
                curPartSize += 1

            ans.append(head)
            for _ in range(curPartSize - 1):  # Skip curPartSize-1 times
                head = head.next

            if head is None: break
            head.next, head = None, head.next  # Split the current part, and go next

        while len(ans) < k: ans.append(None)  # Fill to get enough k parts
        return ans
        """

        # Solution 2 -  20 ms
        def length(x):
            ans = 0
            while x is not  None:
                x = x.next
                ans += 1
            return ans

        ans = []
        l = length(head)
        c = [l // k] * k
        excess = l - (l // k) * k
        for i in range(k):
            if excess >= 1:
                c[i] += 1
                excess -= 1
        cur = head
        for i in range(k):
            ans.append(cur)
            cur = self.find(cur, c[i])
        return ans


# Main Call
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
k = 5
solution = Solution()
split_node = solution.splitListToParts(head, k)
print(split_node)
