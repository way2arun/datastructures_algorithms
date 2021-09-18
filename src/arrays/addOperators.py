"""
Expression Add Operators
Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.



Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []


Constraints:

1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
   Hide Hint #1
Note that a number can contain multiple digits.
   Hide Hint #2
Since the question asks us to find all of the valid expressions, we need a way to iterate over all of them. (Hint: Recursion!)
   Hide Hint #3
We can keep track of the expression string and evaluate it at the very end. But that would take a lot of time. Can we keep track of the expression's value as well so as to avoid the evaluation at the very end of recursion?
   Hide Hint #4
Think carefully about the multiply operator. It has a higher precedence than the addition and subtraction operators.
1 + 2 = 3
1 + 2 - 4 --> 3 - 4 --> -1
1 + 2 - 4 * 12 --> -1 * 12 --> -12 (WRONG!)
1 + 2 - 4 * 12 --> -1 - (-4) + (-4 * 12) --> 3 + (-48) --> -45 (CORRECT!)
   Hide Hint #5
We simply need to keep track of the last operand in our expression and reverse it's effect on the expression's value while considering the multiply operator.

"""
from collections import defaultdict
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # Solution 1 - 724 ms
        """
        def dfs(idx, path, value, last):
            if idx == n and value == target:
                ans.append(path)

            for i in range(idx + 1, n + 1):
                tmp = int(num[idx: i])
                if i == idx + 1 or (i > idx + 1 and num[idx] != "0"):
                    if last is None:
                        dfs(i, num[idx: i], tmp, tmp)
                    else:
                        dfs(i, path + '+' + num[idx: i], value + tmp, tmp)
                        dfs(i, path + '-' + num[idx: i], value - tmp, -tmp)
                        dfs(i, path + '*' + num[idx: i], value - last + last * tmp, last * tmp)

        ans, n = [], len(num)
        dfs(0, "", 0, None)
        return ans
        """
        # Solution 2 - 56 ms
        if not num: return []

        # set the boolean for reusing the func(main search and creating DP)
        def bfs(num, cutEdge=False):
            firstValue = int(num[0])
            # (pre-result, pre-Sum, pre-operation, pre-Number's value)
            queue = [(num[0], firstValue, firstValue, firstValue)]

            for i, c in enumerate(num):
                if i == 0: continue
                newQ, v = [], int(c)
                for preString, preSum, preOP, preNum in queue:
                    # combine with previous num without operator
                    if preString[-1] != '0' or (len(preString) > 1 and preString[-2] not in ('-', '+', '*')):
                        # preOP / preNum * v: extract pre-operation to operate with current value
                        curOP = preOP * 10 + preOP / preNum * v
                        curSum = preSum - preOP + curOP
                        curVal = preNum * 10 + v
                        newQ.append([preString + c, curSum, curOP, curVal])

                    # if current maximal possible num is less than remaining sum,
                    # there's no result because only multiplication can create maximal num.
                    # use this line when main search, not creating DP
                    if not cutEdge and max(1, abs(preOP)) * int(num[i:]) < abs(target - preSum):
                        continue

                    # new search of "*", "+", "-"
                    newQ.append([preString + '*' + c, preSum - preOP + preOP * v, preOP * v, v])
                    if num[i:] not in preview:
                        newQ.append([preString + '+' + c, preSum + v, v, v])
                        newQ.append([preString + '-' + c, preSum - v, -v, v])

                    # check and combine second part's results of "+" and "-" when main search
                    if not cutEdge and i >= len(num) - half:
                        restSum = target - preSum
                        # if able to achieve target, + second part's result directly
                        if restSum in preview[num[i:]]:
                            for parse in preview[num[i:]][restSum]:
                                parseResult.append(preString + "+" + parse)
                        # we can reverse the results in DP for "-",
                        if -restSum in preview[num[i:]]:
                            for parse in preview[num[i:]][-restSum]:
                                parse = parse.replace("-", " ").replace("+", "-").replace(" ", "+")
                                parseResult.append(preString + "-" + parse)
                queue = newQ

            # collect cut edge results(DP)
            if cutEdge:
                result = defaultdict(list)
                for element in queue:
                    result[element[1]].append(element[0])
                return result

            # main BFS's result
            else:
                return queue

            # cut string into two halves for preview(DP table)

        # { key string: { combination value: possible combination} }
        preview = {}
        half = len(num) // 2 + 1
        for i in range(-half, 0):
            preview[num[i:]] = bfs(num[i:], True)

        parseResult = []
        return [e[0] for e in bfs(num) if e[1] == target] + parseResult


# Main Call
num = "105"
target = 5
solution = Solution()
print(solution.addOperators(num, target))
