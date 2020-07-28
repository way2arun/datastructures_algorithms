"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3404/
Task Scheduler
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Solution 1 - 604 ms
        """
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        max_freq_ele_count = 0  # total_elements_with_max_freq, last row elements
        i = 0
        while i < len(freq):
            if freq[i] == max_freq:
                max_freq_ele_count += 1
            i += 1

        ans = (max_freq - 1) * (n + 1) + max_freq_ele_count

        return max(ans, len(tasks))
        """
        # Solution 2 - 384 ms

        if n == 0:
            return len(tasks)

        count = collections.Counter(tasks)
        most = None
        for key, c in count.items():
            if not most or count[most] < c:
                most = key

        c_most = 0
        for key in count:
            if count[key] == count[most]:
                c_most += 1
        ans = (count[most] - 1) * (n + 1) + c_most
        return ans if ans > len(tasks) else len(tasks)


        # Solution 3 = 388 ms
        """
        cnt = list(collections.Counter(tasks).items())
        sorted_cnt = sorted(cnt, key=lambda x: x[1], reverse=True)

        slots = (sorted_cnt[0][1] - 1) * (n + 1)
        for k, v in sorted_cnt:
            slots -= min(v, sorted_cnt[0][1] - 1)
        return len(tasks) + (slots if slots > 0 else 0)
        """


# Main Call
tasks = ["A", "A", "A", "B", "B", "B"]
n = 0
solution = Solution()
print(solution.leastInterval(tasks, n))