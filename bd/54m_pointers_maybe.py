class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h = len(matrix[0])-1
        v = len(matrix)-1

        res = []

        x, y = 0, 0
        direction = [1,0]
        hwall = h
        vwall = 0
        htimes = 0
        vtimes = 0

        # loop while no h & v walls
        while len(res) < (h+1) * (v+1):
            res.append(matrix[y][x])
            if x == hwall and y == vwall:
                # change dir
                if direction == [1,0]:
                    direction = [0,1]
                    vwall = v - vtimes
                elif direction == [0,1]:
                    direction = [-1,0]
                    hwall = 0 + htimes
                elif direction == [-1,0]:
                    direction = [0,-1]
                    vtimes+=1
                    vwall = 0 + vtimes
                elif direction == [0,-1]:
                    direction = [1,0]
                    htimes+=1
                    hwall = h - htimes
                # change wall
            
            x, y = x + direction[0], y + direction[1]
        
        return res
'''
[x,y]

right   [h,0]
down    [h,v]
left    [0,v]
up      [0, 0+1]

right   [h-1, 0+1]
down    [h-1, v-1]
left    [0+1, v-1]
up      [0+1, 0+2]
'''
'''
start horizontal
    [h changes][v static]
    last horizontal position
    [h static][v changes]
    last vertical position
    [h changes][v static] (h change should change dir when it is at a wall)
    last horizontal pos
    [h static][v changes]
    last vertical pos (vertical wall is changed) #when did it change?/ when do we record this change?
    [h changes][v static]
    last horizontal pos (horizontal wall is changed)
    tries to go vertical, but there is a vertical wall.
    end.

'''
