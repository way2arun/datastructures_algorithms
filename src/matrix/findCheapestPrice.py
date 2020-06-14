"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3360/
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.


Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        flight_dict = dict()
        result = []

        # to make a dictionary from edges
        for i in flights:
            if i[0] not in flight_dict:
                flight_dict[i[0]] = [(i[1], i[2])]

            else:
                flight_dict[i[0]].append((i[1], i[2]))

        # BFS
        destinations = [[src, 0]]
        transit_dict = dict()
        while K >= 0 and destinations:
            # to find destinations
            for i in destinations:
                if i[0] in flight_dict:
                    for j in flight_dict[i[0]]:
                        if j[0] == dst:
                            result.append(j[1] + i[1])  # to collect the costs from src to dst
                        else:
                            if j[0] not in transit_dict:
                                transit_dict[j[0]] = j[1] + i[1]
                            # we need the minimum cost only for each transit
                            else:
                                transit_dict[j[0]] = min(transit_dict[j[0]], j[1] + i[1])
            destinations = []
            for i in transit_dict:
                destinations.append([i, transit_dict[i]])
            K -= 1

        if not result:
            return -1

        return min(result)
        """
        # Solution 2
        # Build the adjacency matrix
        graph = defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))

        # Shortest distances array
        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0

        # Data is (cost, stops, node)
        minHeap = [(0, 0, src)]

        while minHeap:

            cost, stops, node = heapq.heappop(minHeap)

            # If destination is reached, return the cost to get here
            if node == dst:
                return cost

            # If there are no more steps left, continue
            if stops == K + 1:
                continue

            # Examine and relax all neighboring edges if possible
            for nei, price in graph[node]:
                dU, dV, wUV = cost, distances[nei], price

                # Better cost?
                if dU + wUV < dV:
                    distances[nei] = dU + wUV
                    heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                elif stops < current_stops[nei]:

                    #  Better steps?
                    current_stops[nei] = stops
                    heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))

        return -1 if distances[dst] == float("inf") else distances[dst]


# Main Call
n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1
solution = Solution()
print(solution.findCheapestPrice(n, edges, src, dst, k))
