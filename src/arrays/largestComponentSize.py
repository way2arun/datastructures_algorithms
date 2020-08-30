"""
Largest Component Size by Common Factor
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3442/
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.



Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000
"""
from collections import Counter
from math import sqrt
from typing import List


class UnionFind():
    def uf(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while x != self.uf[x]:
            self.uf[x] = self.uf[self.uf[x]]
            x = self.uf[x]
        return self.uf[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.uf[x_root] = y_root
        self.size[y_root] += self.size[x_root]
        self.size[x_root] = 0


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # Solution 1 - 3308 ms
        """
        d = {}  # simple union find data structure

        def find(x):
            if x != d.setdefault(x, x):
                d[x] = find(d[x])
            return d[x]

        def union(x, y):
            d[find(x)] = find(y)

        for n in A:
            for i in range(2, int(n ** 0.5) + 1):  # just connect all the factors of the number  to the number
                if n % i:
                    continue
                union(n, i)
                union(n, n // i)

        counter = Counter(find(i) for i in A)
        return max(counter.values())  # return the parent with maximum children
        """

        # Solution 2 - 1352 ms
        def primeFactors(n):  # Prime factor decomposition
            out = set()
            while n % 2 == 0:
                out.add(2)
                n //= 2
            for i in range(3, int(sqrt(n)) + 1, 2):
                while n % i == 0:
                    out.add(i)
                    n //= i
            if n > 2:
                out.add(n)
            return out

        uf = UnionFind()
        uf.uf(len(A))

        primeToIndex = {}
        for i, a in enumerate(A):
            primes = primeFactors(a)
            for p in primes:
                if p in primeToIndex:
                    uf.union(i, primeToIndex[p])
                primeToIndex[p] = i
        return max(uf.size)


# Main Call
solution = Solution()
A = [4, 6, 15, 35]
print(solution.largestComponentSize(A))
