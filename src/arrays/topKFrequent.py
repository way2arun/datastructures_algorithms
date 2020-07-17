"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3393/
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""
import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1 - 152 ms
        """
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        frequency = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)
        result = []
        for n in range(k):
            result.append(frequency[n][0])
        return result
        """
        # Solution 2 - 80 ms
        """
        if k == len(nums):
            nums
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
        """
        # Solution 3 - 72 ms
        cnt = collections.Counter(nums)
        cnt = [(v[1], v[0]) for v in cnt.items()]
        pq = []
        for v in cnt:
            if len(pq) < k:
                heapq.heappush(pq, v)
            else:
                heapq.heappushpop(pq, v)
        ans = []
        while pq:
            ans.append(heapq.heappop(pq)[1])
        return reversed(ans)


# Main Call
nums = [1, 1, 1, 2, 2, 3]
k = 2
solution = Solution()
results = solution.topKFrequent(nums, k)
print(results)
# For Solution 2
for result in results:
    print(result)
