class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)] # SENW

        c = len(grid[0])
        r = len(grid)
        queue = deque()
        queue.append((0,0,0,k))
        seen = set() # seen states of x,y and k.
        # Can't get shorter path with the same k as that requires consuming charges of k.
        # In an empty field and permutation of steps to reach the same coordinates are always equal in length (because we cannot backtrack)

        while queue:
            x,y, steps, kt = queue.popleft()
            if (x,y) == (c-1,r-1):
                return steps
            for d in directions:
                xt, yt = x + d[0], y + d[1]
                if 0 <= xt < c and 0 <= yt < r and (xt,yt,kt) not in seen:
                    if grid[yt][xt] == 1 and kt>0:
                        seen.add((xt,yt,kt))
                        queue.append((xt,yt,steps+1,kt-1))
                    elif grid[yt][xt] == 0:
                        seen.add((xt,yt,kt))
                        queue.append((xt,yt,steps+1,kt))

        return -1
'''
BFS is just queue behaviour with
early termination
special conditions on valid traversal

Time: R*C*K for the number of states we traverse
Space: R*C*K for the number of states we save
Technically k+1 because k can be 0, there are k+1 valid states
'''
