"""
Create Sorted Array through Instructions
Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:

The number of elements currently in nums that are strictly less than instructions[i].
The number of elements currently in nums that are strictly greater than instructions[i].
For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums. Since the answer may be large, return it modulo 109 + 7



Example 1:

Input: instructions = [1,5,6,2]
Output: 1
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
The total cost is 0 + 0 + 0 + 1 = 1.
Example 2:

Input: instructions = [1,2,3,6,5,4]
Output: 3
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.
Example 3:

Input: instructions = [1,3,3,3,2,4,2,1,2]
Output: 4
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.


Constraints:

1 <= instructions.length <= 105
1 <= instructions[i] <= 105
   Hide Hint #1
This problem is closely related to finding the number of inversions in an array
   Hide Hint #2
if i know the position in which i will insert the i-th element in I can find the minimum cost to insert it
"""
import collections
from typing import List

MOD = 10 ** 9 + 7


class FenwickTree:
    def __init__(self, N):
        self.ft = [0] * (N + 1)
        self.N = N

    def update(self, i):
        while i <= self.N:
            self.ft[i] += 1
            i += i & -i

    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.ft[i]
            i -= i & -i

        return ret

def update(arr, val):
    lt_count = 0
    left, right = 0, len(arr)
    while True:
        mid = (left + right) // 2
        node = arr[mid]
        if val == node[0]:
            node[1] += 1
            lt_count += node[2]
            return lt_count, node[1]
        elif val < node[0]:
            node[2] += 1
            right = mid
        else:
            lt_count += node[1] + node[2]
            left = mid + 1

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        # Key idea of the tree: at each node we record the number of values that got added
        # under and including this node so that at some node `u`, you can query `u.left.subtree_size`
        # to find out how many values added that are strictly less than `u` and `u.right.subtree_size`
        # for how may strictly less than `u`.
        self.subtree_size = 0
        # Since there are duplicate values in instructions, each node in the tree could
        # represent multiple instances of the same value added to the tree
        self.inst_cnt = 0


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        # Solution 1 - 8768 ms
        """"
        def build_tree(values, first, last):
            if first > last:
                return None

            mid = (first + last) // 2
            # Since values is sorted, we can use the middle element as the subtree root
            # and ensure its left and right tree have equal number of elements. Or if you are
            # some maniac who got nothing better to do, you could implement an AVL tree or
            # Red-Black tree. Your choice!
            root = Node(values[mid])
            root.left = build_tree(values, first, mid - 1)
            root.right = build_tree(values, mid + 1, last)
            return root

        def mark_added(root, v):
            if v < root.val:
                mark_added(root.left, v)
            elif v > root.val:
                mark_added(root.right, v)
            else:
                root.inst_cnt += 1

            # This is a common pattern in augmented trees where we propogate the count of
            # of elements from the children up towards the root such that each time a
            # new element is added below the root of some subtree, we update at the root
            # the count so one could immediately query the size of the subtree without
            # exploring all the nodes of the subtree each time
            root.subtree_size += 1

        # Build a balanced tree using the list of sorted, unique values in instructions.
        # NOTE the elements merely form the tree, they aren't officially marked as added
        # until we call mark_added() that'd update `inst_cnt` and `subtree_size` for each
        # node to indicate that the value was indeed added
        values = sorted(collections.Counter(instructions).keys())
        root = build_tree(values, 0, len(values) - 1)

        p = 10 ** 9 + 7
        cost = 0
        for v in instructions:
            mark_added(root, v)

            # After the new value has been marked as added, it just a matter of traversing the
            # tree one more time until we reach `v` and note the `subtree_size` along the way
            # and add up how many values in the tree is either stricly less than `v` or greater than `v`
            curr = root
            nb_gt = 0
            nb_less = 0
            while v != curr.val:
                if v < curr.val:
                    nb_gt += (curr.right.subtree_size if curr.right != None else 0) + curr.inst_cnt
                    curr = curr.left
                elif v > curr.val:
                    nb_less += (curr.left.subtree_size if curr.left != None else 0) + curr.inst_cnt
                    curr = curr.right
            nb_less += curr.left.subtree_size if curr.left != None else 0
            nb_gt += curr.right.subtree_size if curr.right != None else 0
            cost = (cost % p + min(nb_gt, nb_less) % p) % p

        return cost % p
        """
        # Solution 2 - 4040 ms
        """
        m = max(instructions)
        arr = [0 for _ in range(m + 1)]

        def update(x):
            while x <= m:
                arr[x] += 1
                x += x & -x

        def get(x):
            res = 0
            while x > 0:
                res += arr[x]
                x -= x & -x
            return res

        cost = 0
        for idx, instruction in enumerate(instructions):
            cost += min(get(instruction - 1), idx - get(instruction))
            update(instruction)
        return cost % (10 ** 9 + 7)
        """
        # Solution 3 - 3920 ms
        """
        arr = [[v, 0, 0] for v in sorted(list(set(instructions)))]
        if len(arr) <= 2:
            return 0
        result = 0
        for i, x in enumerate(instructions):
            lt_count, eq_count = update(arr, x)
            result += min(lt_count, i + 1 - lt_count - eq_count)
        return result % 1000000007
        """
        # Solution 4 - 3784 ms
        """
        arr = [[v, 0, 0] for v in sorted(list(set(instructions)))]
        if len(arr) <= 2:
            return 0
        result = 0
        for i, x in enumerate(instructions):
            lt_count = 0
            left, right = 0, len(arr)
            while True:
                mid = (left + right) // 2
                node = arr[mid]
                if x == node[0]:
                    node[1] += 1
                    lt_count += node[2]
                    result += min(lt_count, i + 1 - lt_count - node[1])
                    break
                elif x < node[0]:
                    node[2] += 1
                    right = mid
                else:
                    lt_count += node[1] + node[2]
                    left = mid + 1
        return result % 1000000007
        """
        # Solution 5 - 3500  ms
        N = max(instructions)
        ft = FenwickTree(N)
        cost = 0

        for x in instructions:
            cost_smaller = ft.query(x - 1)
            cost_larger = ft.query(N) - ft.query(x)
            cost += min(cost_smaller, cost_larger)
            cost %= MOD
            ft.update(x)

        return cost




# Main Call
instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]

solution = Solution()
print(solution.createSortedArray(instructions))
