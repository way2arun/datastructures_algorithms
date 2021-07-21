"""
Push Dominoes
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.



Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."


Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Solution 1 - 264 ms
        """
        res = ""  # Used to store final result.
        i = 0
        while i < len(dominoes):
            # if charAt(i) is 'L' or 'R', just place append the same in res.
            if dominoes[i] == 'L' or dominoes[i] == 'R':
                res += dominoes[i]
                i += 1
            else:  # dominoes[i]=='.':
                # if charAt(i) is '.' and previous is Right pushed then, we have to count the
                # number of '.' (dots) and see what is at the other end of dot.
                if i > 0 and dominoes[i - 1] == 'R':
                    j = i
                    while j < len(dominoes) and dominoes[j] == '.':
                        j += 1
                    countDots = (j - i)  # count of number of '.'(dots)
                    # if the other end is last index or if dominoe at other end is right pushed then
                    # there is nothing to cancel the right pushed force of first dominoes and so all
                    # '.'(dots) will be rightly pushed
                    if j == len(dominoes) or dominoes[j] == 'R':
                        res += 'R' * countDots
                    else:  # if other end is 'L' i.e, left pushed
                        # first half will be rightly pushed and second half is leftly pushed and
                        # if count is odd, then force on middle one gets cancelled
                        res += 'R' * (countDots // 2) + '.' * (countDots - 2 * (countDots // 2)) + 'L' * (
                                    countDots // 2)
                    i = j
                else:  # if the start of string is '.'(dot) or previous is not rightly pushed
                    j = i
                    while j < len(dominoes) and dominoes[j] == '.':
                        j += 1
                    countDots = (j - i)  # count the number of dots

                    # if the other end is last index or if dominoe at other end is right pushed
                    # then there is no force at all on stating indexes. So, all will remains '.'
                    if j == len(dominoes) or dominoes[j] == 'R':
                        res += '.' * countDots
                    # if other end is left pushed, the all the starting will be pushed left
                    else:
                        res += 'L' * countDots
                    i = j

        return res
        """
        # Solution 2 - 72 ms
        result = ""

        buffer_count = 0

        is_falling_right = False

        for c in dominoes:
            if c == ".":
                buffer_count += 1

            elif c == 'L':
                if is_falling_right:
                    q, r = divmod(buffer_count + 1, 2)

                    result += "R" * q + ("" if r == 0 else ".") + "L" * q

                    buffer_count = 0
                    is_falling_right = False
                else:
                    result += "L" * (buffer_count + 1)
                    buffer_count = 0

            elif c == 'R':
                if is_falling_right:
                    result += 'R' * buffer_count
                    buffer_count = 1
                    is_falling_right = True
                else:
                    result += "." * buffer_count
                    buffer_count = 1
                    is_falling_right = True

        if buffer_count != 0:
            if is_falling_right:
                c = 'R'
            else:
                c = '.'
            result += c * buffer_count

        return result


# Main Call
dominoes = ".L.R...LR..L.."
solution = Solution()
print(solution.pushDominoes(dominoes))