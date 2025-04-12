"""
Max island series:
1. Find the max-island
2. Find the max-new-island by flipping at most one 0 to 1
3. Find the max-new-island that is independent from existing islands


#1. Simple BFS traversal on any unvisited 1s
    - update max area on the way

#2. Simple BFS, label each islands by island id, and keep a hashmap of {id: area}
   - then for all 0s, check for adjacent island areas + 1 to update max new area

#3. Simple BFS again, but we first find banned 0s first, mark them somehow (new matrix, or maybe label mark -1 inplace)
   - then for all non-visited, non-banned 0s, do the BFS again, marking visited along the way,
     update for maximum new island size.
   - defualt would be 0 if no such area is found (because of the existing islands maybe)
"""

# variant 3 implementation
from typing import List
from collections import deque


class Solution:
    # Assuming inplace-mutation is allowed
    def find_max_new_island_area(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        max_new_area = 0

        visited = [[False] * N for _ in range(M)]

        # 1. mark banned area
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    # adjacent 0s only
                    for dx, dy in [(1, 0), (-1, 0), (0,1), (0,-1)]:
                        new_x, new_y = i+dx, j+dy
                        if (0 <= new_x < M and 0 <= new_y < N 
                            and grid[new_x][new_y] == 0 
                        ):
                            grid[new_x][new_y] = -1 # mark invalid

        # BFS helper, computing new area
        def bfs(x, y): # start from x, y
            q = deque([(x, y)])
            visited[x][y] = True
            area = 1
            while q:
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < M and 0 <= nc < N and
                        grid[nr][nc] == 0 and not visited[nr][nc]
                    ):
                        visited[nr][nc] = True
                        area += 1
                        q.append((nr, nc))
            return area

        # 2. for each valid 0s, traverse BFS, find max area
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0 and not visited[i][j]:
                    max_new_area = max(max_new_area, bfs(i, j))

        return max_new_area



if __name__=="__main__":
    sample_grid = [[1, 0, 0, 0, 1],
                   [1, 0, 0, 0, 1],
                   [1, 1, 0, 1, 1]]
    print("Given:")
    for row in sample_grid:
        print(row)
    print(f"Result: {Solution().find_max_new_island_area(sample_grid)}")
    print("Answer is : 2")
