"""
Generate Random Point in a Circle
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
Example 1:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
Example 2:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""
from cmath import sqrt, cos, sin, pi
from random import uniform, random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        # Solution 1 - 152 ms
        """
        self.r, self.x, self.y = radius, x_center, y_center
        """
        # Solution 2 - 120 ms
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Solution 1 - 152 ms
        """
        theta = uniform(0, 2 * pi)
        R = self.r * sqrt(uniform(0, 1))
        return [self.x + R * cos(theta), self.y + R * sin(theta)]
        """
        # Solution 2 - 120 ms
        radius = self.radius * sqrt(random())  # sample radius as r*sqrt(x)
        theta = 2 * pi * random()  # sample angle as unif [0, 2*pi)
        return self.x_center + radius * cos(theta), self.y_center + radius * sin(theta)


# Main Call
radius = 10
x_center = 5
y_center = -7.5

obj = Solution(radius, x_center, y_center)
param_1 = obj.randPoint()
print(param_1)