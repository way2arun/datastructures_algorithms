"""
Number of Subarrays with Bounded Maximum
We are given an array nums of positive integers, and two positive integers left and right (left <= right).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

Example:
Input:
nums = [2, 1, 4, 3]
left = 2
right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

left, right, and nums[i] will be an integer in the range [0, 109].
The length of nums will be in the range of [1, 50000].
"""
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # Solution 1 - 324 ms
        """
        ans, low, mid = 0, 0, 0
        for num in nums:
            if num > right:
                mid = 0
            else:
                mid += 1
                ans += mid
            if num >= left:
                low = 0
            else:
                low += 1
                ans -= low
        return ans
        """
        # Solution 2- 300 ms
        # We have to find the number of subarrays such that the maximum element in window is greater-equal to left
        # and less than equal right
        # basically    left <= maximum_element_in_window <= right

        # ---------------------------THEORY----------------------------------------------------------
        # contiguous subarrays in this case will be added like so.
        # if left = 2, right = 4 and array = [0, 3, 1, 2]
        #
        #                                   0, 3, 1, 2, 0, 5, 1, 2
        # window_opening =>                 ^
        # window_closing =>                          ^
        #
        # number of contiguous subarrays satisfying condition to have a NEEDED ELEMENT AT THE CLOSING is
        # equal to the length of window. Because the window_ending always has to be there in the subarray
        #
        #                   0, 3, 1, 2
        #                   ---------- [0, 3, 1, 2]
        #                      -------    [3, 1, 2]
        #                         ----       [1, 2]
        #                            -          [2]
        #
        # similarly when window closing was at 3 before this iteration
        #
        #
        #                                   0, 3, 1, 2, 0, 5, 1, 2
        # window_opening =>                 ^
        # window_closing =>                    ^
        #
        # we would add the length of window with A NEEDED ELEMENT at window closing becuase we needed all the
        # subarrays with 3 present. And A NEEDED ELEMENT IS ALWAYS AT THE END HERE. Becuase we calcualte as soon
        # as we encounter it
        #
        #
        #                   0, 3
        #                   ---- [0, 3]
        #                      -    [3]
        # -----------------------------------------------------------------------------------------------------

        # Classification => NEEDED ELEMENTS, numbers such that      left <= number <= right
        #                   OKAY ELEMENTS, numbers such that        number < left
        #                   NOT OKAY ELEMENTS, numbers such that    number > right

        # window opening
        window_opening = 0

        # result. That stores number of subarrays with bounded maximum
        result = 0

        # temp_score. Similar to backlog_counter from nice subarrays problem.
        temp_score = 0

        for index, number in enumerate(nums):
            # if number is a NEEDED ELEMENT
            if left <= number <= right:
                # we set temp_score to window_length
                temp_score = index - window_opening + 1

                # we add temp_score to result
                result += temp_score

            # elif number is an OKAY ELEMENT
            elif number < left:
                # we add the temp_score to result
                result += temp_score

            # else if number is a NOT OKAY ELEMENT
            else:
                # we set window_opening to one index after this index
                window_opening = index + 1

                # we reset temp_score to 0
                temp_score = 0

        return result


# Main Call
solution = Solution()
nums = [2, 1, 4, 3]
left = 2
right = 3
print(solution.numSubarrayBoundedMax(nums, left, right))
