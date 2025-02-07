class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # T: O(m * n), S: O(m * n)
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = [[False] * cols for _ in range(rows)]
        atlantic_reachable = [[False] * cols for _ in range(rows)]

        def dfs(r, c, reachable):
            reachable[r][c] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not reachable[nr][nc]
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, reachable)

        # Start DFS from Pacific (top and left edges)
        for c in range(cols):
            dfs(0, c, pacific_reachable)  # Top row
            dfs(rows - 1, c, atlantic_reachable)  # Bottom row

        for r in range(rows):
            dfs(r, 0, pacific_reachable)  # Left column
            dfs(r, cols - 1, atlantic_reachable)  # Right column

        # Collect results
        result = [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if pacific_reachable[r][c] and atlantic_reachable[r][c]
        ]

        return result
