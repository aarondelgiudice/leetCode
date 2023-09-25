"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two
different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one
direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of
edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:
2 <= n <= 5 * 10**4
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi

source: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""

from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # bredth first search from city 0
        # hashSet
        edges = {(a, b) for a, b in connections}
        print(edges)

        # find each nodes neighbors
        neighbors = {city: [] for city in range(n)}

        # we only want to visit each node once
        # use a hashSet to keep track of visited nodes
        visited = set()

        # track changes to edges
        changes = 0

        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visited, changes
            
            visited.add(city)
            
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                
                # check if neighbor can reach city zero
                if (neighbor, city) not in edges:
                    changes += 1

                visited.add(neighbor)

                dfs(neighbor)

        dfs(0)

        return changes

if __name__ == "__main__":
    INPUTS = (
        # n,    connections,                        expected
        (6,     [[0,1],[1,3],[2,3],[4,0],[4,5]],    3),
        (5,     [[1,0],[1,2],[3,2],[3,4]],          2),
        (3,     [[1,0],[2,0]],                      0),
    )

    for n, connections, expected in INPUTS:
        actual = Solution().minReorder(n, connections)
        assert actual == expected, f"minReorder({n}, {connections}) == {actual}, expected {expected}"
