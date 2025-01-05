class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:     

        if grid[0][0]==1 or grid[-1][-1]==1: return -1
                
        path = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        n = len(grid)
        queue = [(0,0,1)]

        while queue:
            row, col, steps = queue.pop(0)

            if row==n-1 and col==n-1: return steps

            for dr, dc in path:
                r=row+dr
                c=col+dc

                if 0<=r<n and 0<=c<n and grid[r][c]==0:
                    queue.append((r,c,steps+1))
                    grid[r][c]=1
        return -1
