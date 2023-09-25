"""
You are given an m x n grid grid where:
'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.

You start at the starting point and one move consists of walking one space in one of the four cardinal
directions. You cannot walk outside the grid, or walk into a wall.
If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English
alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that
the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:
Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.

Example 2:
Input: grid = ["@..aA","..B#.","....b"]
Output: 6

Example 3:
Input: grid = ["@Aa"]
Output: -1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.

source: https://leetcode.com/problems/shortest-path-to-get-all-keys/
"""

from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # helper functions
        def has_key(char, key):
            """
            Check if we currently hold a key.
            First check what position in our key bit array will the key for the char/lock be in.
            Then right shift the key by the same number of positions and check if the right
            most bit is 1.
            
            example:
                if we want to check if we have key for C and our key bit array looks like this
                    10100 
                C will be at position 2 since ord('C') - ord('A') == 2.
                Then our key will look like this
                    00101.
                Notice how the 1 at position 2 moved by 2 positions so 00101 adding by 1
                will give 
                us 1 which means key for C is present.
            """
            v = ord(char) - ord('A')
            key = key >> v # key = key * 2**v

            # bitwise AND is 1 only if both of its inputs are 1, otherwise it's 0.
            key = key & 1

            return key == 1

        def add_key(char, key):
            """
            flip a bit from 0->1 depending on the character a->f.
            Left shift 1 by the same number of places and do a OR operation on the bit so it
            flips to 1.

            example
                we want to add a key for c and our key bit array looks like this
                    10001
                c will be at position 2 since ord('C') - ord('A') == 2.
                Shifting 1 by 2 bits converts it from 00001 to 00100.
                Now if we 00100 AND 10001 we get 10101. So now we know we have keys for A, C and E.
            """
            v = ord(char) - ord('a')
            temp = 1 << v # temp = 1 * 2**v

            # bitwise OR is 1 if one or both of its inputs are 1, otherwise it's 0.
            key = key | temp
            
            return key

        def add_neighbors(row, col, keys, queue, visited):
            """
            there are only 4 directions we can go, so keep adding those adjacent cells to
            our queue.
            to avoid doing any duplicate calculations
                - We can avoid visiting cells that we have visited
                - If a cell is a wall, then don't add it to queue
                - Otherwise if the cell will be out of bounds then don't add it.

            Otherwise add it to queue.
            """
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            dist = visited[(row, col, keys)]
            
            for r, c in dirs:
                if (row+r, col+c, keys) in visited:
                    continue
            
                if row+r == -1 or col+c == -1 or row+r == len(grid) or col+c == len(grid[0]):
                    continue
            
                if grid[row+r][col+c] == "#":
                    continue
            
                queue.append((row+r, col+c, keys))
                visited[(row+r, col+c, keys)] = dist + 1
            
            return

        def helper(i, j, total_keys):
            """
            Breadth First search
            maintain a queue of tuples of (position i, position j, total keys)
            and a dictionary, visited, of
                {((position i, position j, total keys)): distance}
            """
            # Here i,j is the starting point @ and 0 since we do not have any keys,
            # and 0 distance since we start from 0.
            queue = [(i,j,0)]
            visited = {(i,j,0):0}
            
            while len(queue) > 0:
                # At every iteration get the row, col, keys from our queue
                row, col, keys = queue.pop(0)
            
                # at every iteration we want to check if all keys are found
                if keys == (1 << total_keys) - 1:
                    return visited[(row, col, keys)]-1
            
                # check cell type: lock, key, wall
                cell = grid[row][col]
            
                if cell.isupper(): # Cell is a lock
                    # check if we have the key
                    # if yes, we can add the cell neighbors
                    if has_key(cell, keys):
                        add_neighbors(row, col, keys, queue, visited)
            
                    # if no, go to the next i, j position
                    else:
                        continue
            
                # if cell is . or @ then add all possible neighbors.
                elif cell == "." or cell == "@":
                    add_neighbors(row, col, keys, queue, visited)
            
                # else, cell is a key
                elif cell.islower():
                    # get distance previous state
                    dist = visited[(row, col, keys)]
                    # add the 1 between postion 0->6 in keys depending on the cell is a->f.
                    keys = add_key(cell, keys)
                    # update distance to new state (row, col, keys)
                    visited[(row, col, keys)] = dist

                    # add all neighbors
                    add_neighbors(row, col, keys, queue, visited)
            
            return -1
    
        # First loop over all the cells in grid to get our starting positions and number of
        # keys
        start = [-1,-1]
        total_keys = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '@':
                    start = [i,j]
                
                if grid[i][j].islower():
                    total_keys += 1

        return helper(start[0], start[1], total_keys)


if __name__ == "__main__":
    INPUTS = (
        # grid: List[str]           expected: int
        (["@.a..","###.#","b.A.B"], 8),
        (["@..aA","..B#.","....b"], 6),
        (["@Aa"],                   -1),
    )

    for grid, expected in INPUTS:
        actual = Solution().shortestPathAllKeys(grid)
        assert actual == expected, f"{actual=}, {expected=}, {grid=}"
