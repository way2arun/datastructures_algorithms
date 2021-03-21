"""
Reordered Power of 2
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9
"""
from typing import Counter


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # Solution 1 - 36 ms
        """
        # digit <-> occurrence mapping of N
        signature_of_N = Counter(str(N))
        # check each possible power of 2
        for i in range(32):
            # get power of 2 by bitwise operation
            power_of_2 = 1 << i
            if Counter(str(power_of_2)) == signature_of_N:
                # Accept if at least one power of 2's mapping is the same with N's mapping
                return True
        # Reject otherwise
        return False
        """
        # Solution 2 - 24 ms
        n = sorted(str(N))
        for i in range(32):
            x = (1 << i)
            m = sorted(str(x))
            if m == n: return True
        return False


# Main Call
N = 1
solution = Solution()
print(solution.reorderedPowerOf2(N))