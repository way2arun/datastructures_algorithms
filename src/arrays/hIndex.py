"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3364/
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?

   Hide Hint #1
An easy approach is to sort the array first.
   Hide Hint #2
What are the possible values of h-index?
   Hide Hint #3
A faster approach is to use extra space.

"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Solution 1 - 28 ms
        """
        start = 0
        end = len(citations)
        citations.sort()
        while start < end:
            middle = start + (end - start) // 2
            h_index = len(citations) - middle
            if h_index <= citations[middle]:
                end = middle
            else:
                start = middle + 1
        return len(citations) - start
        """
        # Solution 2
        """
        if not citations:
            return 0

        left = 0
        right = len(citations) - 1

        while left < right:
            mid = left + (right - left) // 2

            if citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                right = mid

        return len(citations) - right if citations[right] >= (len(citations) - right) else 0
        """

        # Solution 3 - 16 ms

        if not citations:
            return 0

        citations.sort(reverse=True)
        h = [0]
        for idx, val in enumerate(citations):

            if val >= idx + 1:
                h.append(idx + 1)

        return max(h)
        """

        # Solution 4 - 20 ms
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0
        """


# Main Call
solution = Solution()
citations = [0, 1, 3, 5, 6]
print(solution.hIndex(citations))
