"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3390/
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.



Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0


Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
   Hide Hint #1
The tricky part is determining how the minute hand affects the position of the hour hand.
   Hide Hint #2
Calculate the angles separately then find the difference.
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Solution 1 - 36 ms
        """
        degreeCoveredByOneHr = 30
        degreeCoveredByOneMin = 6

        # base position = 12:00
        # Angle sweeped by minute hand from base position
        angleMadeByMinuteHand = degreeCoveredByOneMin * minutes

        # Angle sweeped by hour hand from base position
        angleMadeByHrHand = (degreeCoveredByOneHr * hour) % 360
        extraAngleByHrHand = (minutes / 60) * degreeCoveredByOneHr

        # Take the difference of two angles
        angle = abs(angleMadeByMinuteHand - (angleMadeByHrHand + extraAngleByHrHand))

        # This is basically done so as to take the shorter angle out of two
        return min(abs(360 - angle), angle)
        """

        # Solution 2 - 12 ms
        # divide minutes by 5
        # difference of numbers 6 apart (180)
        # difference of 3 apart (90)
        # therefore, difference of 1 apart is 30
        # 1 is 30, 2 is 60, 3 is 90, 4 is 120, 5 is 150, 6 is 180, 7 is 150 ..

        # calculate minute angle (minutes * 6)
        minuteAngle = float(minutes * 6)
        hourAngle = (float(hour % 12) * 30.0) + (minutes * 0.5)
        diffAngle = max(hourAngle, minuteAngle) - min(hourAngle, minuteAngle)
        if diffAngle <= 180.0:
            return max(hourAngle, minuteAngle) - min(hourAngle, minuteAngle)
        else:
            return 360 - diffAngle


# Main Call
solution = Solution()
hour = 12
minutes = 30
print(solution.angleClock(hour, minutes))