"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
   Hide Hint #1
Will Brute force work here? Try to optimize it.
   Hide Hint #2
Can we optimize it by using some extra space?
   Hide Hint #3
What about storing sum frequencies in a hash table? Will it be useful?
   Hide Hint #4
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.

https://leetcode.com/submissions/detail/328576431/?from=/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/

"""
import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 88 ms
        '''
            Plan A:
            For each index a and all indices b > a,
              test whether sum(A[a:b+1]) == k
            Time complexity: O(n^2)

            Need a way to group these subarrays;
            the scheme above groups them by the left side

            We could also "grow" these arrays from a given "center";
            this would take O(n) time for a single "center".
            We have to try all the centers.
            Time: O(n^2)

            Ideas:
            could remeember subarrays that sum to zero. (Later)

            Iterative:
            O(n N) time, O(n) space


            Maintain a sorted list of sums of arrays that end at index k
            O(N) = O(n) space
            Insert: O(1) time <-- list reallocation; use linked-list to save this
            Update(val): O(N) time where N is the number of distinct values; O(n)

            Total space: O(n)
            Total time: O(n N) <-- update
            Can use a list to keep the tuples (val, count)

            Divide and Conquer:
            L(a,b):
              - counts sub-intervals of [a,b), and
              - gives a sorted (ascending) list of suffix values
              Time: O(b-a) <-- Really? Why not O(n)?
            R(a,b):
              - counts sub-intervals of [a,b), and
              - gives a sorted (ascending) list of preffix values
              Time: O(b-a) <-- Really? Why not O(n)?

            M(a,c,b):
              - Merges L = L(a,c) and R = R(c,b)
              - kL <-- rank of the smallest L-elem s.t. L[kL] + R[0] > k
              - kR <-- rank of the smallest R-elem s.t. R[kR] + L[0] > k
              - L' = L[:kL], R' = R[:kR]
              - Scan L' in ascending order, and R' in descending order,
                and check whether two values sum to k

              Time: O(log(n)) + O(n)

            Total time: O(n log n) <-- but complicated

            Plan D: hashtable
            Save prefix sums as a hashtable
            Specifically, for each prefix A[:a], psum holds the tuple (sum(A[:a]), count)
            For each b in [:n],
              we check whether psum[b] - k in psum, i.e.,
              whether exists some a in pusm s.t. b - k == a, or b - a == k.
              If so, we increment our cout_k

            '''

        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 1 if nums[0] == k else 0

        count_k = 0
        psum = None
        s = sum(nums)

        def ht():
            nonlocal count_k
            '''
            A = [1,2,1,1,-2,1], k = 3

            b A[b] psum[b] psum[b]-3  count_k    psum added
            ------------------------------------------------
                                        0         0:1
            0   1   1      -2           0         1:1
            1   2   3      0            1         3:1+
            2   1   4      1            2         4:1++ 
            3   1   5      2            2         5:1 
            4  -2   3      0            3         
            5   1   4      1            4         
            '''
            ht = {0: 1}
            running_sum = 0
            for b in nums:
                running_sum += b
                if running_sum - k in ht:
                    count_k += ht[running_sum - k]
                if running_sum in ht:
                    ht[running_sum] += 1
                else:
                    ht[running_sum] = 1

        def brute_force():
            nonlocal count_k, psum
            psum = [nums[i] for i in range(n)]
            for i in range(1, n):
                psum[i] += psum[i - 1]

            for i in range(n):
                offset = (psum[i - 1] if i >= 1 else 0)
                for j in range(i, n):
                    # closed interval [i,j]
                    if psum[j] - offset == k:
                        count_k += 1

        def linear_scan():
            nonlocal count_k
            T = []
            for i, elem in enumerate(A):
                singleton_inserted = False
                for j, (val, count) in enumerate(T):
                    if val == 0:
                        count += 1
                        singleton_inserted = True
                    T[j] = (val + elem, count)
                    if val + elem == k:
                        count_k += count
                if not singleton_inserted:
                    T.append((elem, 1))
                    if elem == k:
                        count_k += 1

        def left(a, b):
            pass

        def right(a, b):
            pass

        # returns the index of the smallest elem
        #   s.t. elem + val > k
        # key is a lambda
        def bs(sorted_arr, val, key=None):
            pass

        # returns the number of occurrences of val
        def count_elem(sorted_arr, elem):
            pass

        # L is a sorted array of tuples (val, count); same is R
        def merge(L, R):
            if not L:
                pass
            elif not R:
                pass
            else:
                kL = bs(L, R[0])  # L[kL] + R[0] > k
                kR = bs(R, L[0])  # R[kL] + L[0] > k

                # merge
                # hash table version: O(n) time and space
                htL = {lval: lcount for lval, lcount in L[:kL]}  # O(n)
                for rval, rcount in R[:kR]:  # O(n)
                    if k - rval in htL:
                        count_k += htL[k - rval] * rcount

        def div_and_conq(left=0, right=None, LR=None):
            if not right:
                right = n

            center = left + (right - left) // 2
            L = div_and_conq(left, center, "L")
            R = div_and_conq(center, right, "R")
            M = merge(L, R)
            if LR == "L":  # this was a left part
                rv = psum[right - 1] - psum[center - 1]
                # problem: multiple values?
                # vvv
                return sorted(
                    R + [(lv + rv, lc) for (lv, lc) in L],
                    key=lambda val, count: val
                )

        # linear_scan()
        # brute_force()
        ht()
        return count_k
        """
        # 116  ms
        check = collections.defaultdict(int)
        value, total = 0
        check[0] += 1
        for num in nums:
            total += num
            value += check[total - k]
            check[total] += 1
        return value
        """

# Main Call
solution = Solution()
nums = [1,1,1]
k = 2
result = solution.subarraySum(nums, k)
print(result)