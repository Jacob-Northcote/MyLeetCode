class Solution(object):
    def minimumArea(self, grid):
        row = len(grid)
        col = len(grid[0])

        highestOne = row
        lowestOne = -1
        LeftOne = col
        RightOne = -1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    highestOne = min(i,highestOne)
                    lowestOne = max(i,lowestOne)
                    LeftOne = min(j,LeftOne)
                    RightOne = max(j,RightOne)
        
        if lowestOne == -1: 
            return 0
        
        return (lowestOne - highestOne + 1) * (RightOne - LeftOne + 1)



        
