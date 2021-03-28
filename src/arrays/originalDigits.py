"""
Reconstruct Original Digits from English
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""
from typing import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        # Solution 1 - 36 ms
        """
        cnt = Counter(s)
        print(cnt)
        idchars = \
            {
                'w': ('two', '2'),
                'u': ('four', '4'),
                'x': ('six', '6'),
                'f': ('five', '5'),
                'z': ('zero', '0'),
                'r': ('three', '3'),
                't': ('eight', '8'),
                's': ('seven', '7'),
                'i': ('nine', '9'),
                'n': ('one', '1')
            }
        digits = []
        for ch, (word, digit) in idchars.items():
            digit_count = cnt[ch]
            digits.append(digit * digit_count)
            for c in word: cnt[c] -= digit_count
        return ''.join(sorted(digits))
        """
        # Solution 2 - 28 ms
        counts = [0] * 10
        counts[0] = s.count('z')
        counts[2] = s.count('w')
        counts[4] = s.count('u')
        counts[6] = s.count('x')
        counts[8] = s.count('g')

        counts[5] = s.count('f') - counts[4]

        counts[1] = s.count('o') - counts[0] - counts[2] - counts[4]
        counts[3] = s.count('r') - counts[0] - counts[4]
        counts[7] = s.count('v') - counts[5]

        counts[9] = s.count('i') - counts[5] - counts[6] - counts[8]

        res = ''.join(str(i) * counts[i] for i in range(10) if counts[i])

        return res


# Main Call
s =  "owoztneoer"
solution = Solution()
print(solution.originalDigits(s))