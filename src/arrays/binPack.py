"""
Bin Packing Problem (Minimize number of used Bins)
Given n items of different weights and bins each of capacity c,
assign each item to a bin such that number of total used bins is minimized.
It may be assumed that all items have weights smaller than bin capacity.

Input:  wieght[]       = {4, 8, 1, 4, 2, 1}
        Bin Capacity c = 10
Output: 2
We need minimum 2 bins to accommodate all items
First bin contains {4, 4, 2} and second bin {8, 2}

Input:  wieght[]       = {9, 8, 2, 2, 5, 4}
        Bin Capacity c = 10
Output: 4
We need minimum 4 bins to accommodate all items.

Input:  wieght[]       = {2, 5, 4, 7, 1, 3, 8};
        Bin Capacity c = 10
Output: 3

Lower Bound
We can always find a lower bound on minimum number of bins required. The lower bound can be given as :

   Min no. of bins  >=  Ceil ((Total Weight) / (Bin Capacity))

In the above examples, lower bound for first example is “ceil(4 + 8 + 1 + 4 + 2 + 1)/10” = 2 and lower bound in second example is “ceil(9 + 8 + 2 + 2 + 5 + 4)/10” = 3.
This problem is a NP Hard problem and finding an exact minimum number of bins takes exponential time. Following are approximate algorithms for this problem.

Applications

Loading of containers like trucks.
Placing data on multiple disks.
Job scheduling.
Packing advertisements in fixed length radio/TV station breaks.
Storing a large collection of music onto tapes/CD’s, etc.

"""


class Solution:
    def nextfit(self, weight, c):
        res = 0
        rem = c
        for _ in range(len(weight)):
            if rem >= weight[_]:
                rem = rem - weight[_]
            else:
                res += 1
                rem = c - weight[_]
        return res

    def firstFit(self, weight, n, c):

        # Initialize result (Count of bins)
        res = 0

        # Create an array to store remaining space in bins
        # there can be at most n bins
        bin_rem = [0] * n

        # Place items one by one
        for i in range(n):

            # Find the first bin that can accommodate
            # weight[i]
            j = 0

            # Initialize minimum space left and index
            # of best bin
            min = c + 1
            bi = 0

            for j in range(res):
                if bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min:
                    bi = j
                    min = bin_rem[j] - weight[i]

                    # If no bin could accommodate weight[i],
            # create a new bin
            if min == c + 1:
                bin_rem[res] = c - weight[i]
                res += 1
            else:  # Assign the item to best bin
                bin_rem[bi] -= weight[i]
        return res

    # Driver Code


weight = [2, 5, 4, 7, 1, 3, 8]
c = 10
n = len(weight)
solution = Solution()
print("Number of bins required in Next Fit :", solution.nextfit(weight, c))
print("Number of bins required in Next Fit :", solution.firstFit(weight, n, c))
