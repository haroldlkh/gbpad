class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        R, C = len(grid), len(grid[0])
        seen = [[False]*C for _ in grid]
        shape = set()

        def dfs(r0,c0,r,c,coords):
            seen[r][c]=True
            coords.append((r-r0,c-c0))
            for dr, dc in ((1,0),(0,1),(-1,0),(0,-1)):
                nr, nc = r+dr, c+dc
                if (0<=nr<R and 0<=nc<C
                    and not seen[nr][nc]
                    and grid[nr][nc]==1):
                    dfs(r0,c0,nr,nc,coords)

        for i in range(R):
            for j in range(C):
                if grid[i][j]==1 and not seen[i][j]:
                    coords=[]
                    dfs(i,j,i,j,coords)
                    shape.add(tuple(sorted(coords)))
        
        return len(shape)
