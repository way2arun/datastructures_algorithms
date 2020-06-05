"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""
import bisect
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):

        self.acc_w = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.acc_w.append(prefix_sum)

    def pickIndex(self) -> int:

        return bisect.bisect(self.acc_w, self.acc_w[-1] * random.random())


# Main Call
# Your Solution object will be instantiated and called as such:
w = [[[1,3]],[],[],[],[],[]]
obj = Solution(w)
param_1 = obj.pickIndex()
print(param_1)
