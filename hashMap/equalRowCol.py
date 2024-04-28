import os
os.system('clear')
import numpy as np
import pandas as pd
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        gridTrans = np.transpose(grid)
        idxRow1 = 0
        idxCol1 = 0
        idxRow2 = 0
        idxCol2 = 0
        numRows = np.shape(grid)[0]
        equal = 0
        while idxRow1 < numRows:
            currentElem = grid[idxRow1][idxCol1]
            while idxRow2 < numRows:
                if currentElem == gridTrans[idxRow2][idxCol2]:
                    flag = 1
                    while idxCol2 < numRows - 1 and flag:
                        idxCol2 += 1
                        currentElem = grid[idxRow1][idxCol2]
                        if currentElem != gridTrans[idxRow2][idxCol2]:
                            flag = 0
                        else:
                            flag = 1
                    if flag:
                        flag = 0
                        equal += 1
                    idxCol1 = 0
                    idxCol2 = 0            
                idxRow2 += 1
                currentElem = grid[idxRow1][idxCol1]
            idxRow2 = 0
            idxRow1 += 1
        return equal
            
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# grid = [[13,13],[13,13]]
# grid = [[3,2,1],[1,7,6],[2,7,7]]
# grid = [[8,6,3,3,19,6,12,8,4],[10,14,2,16,5,14,10,11,16],[9,20,15,3,10,20,6,12,13],[14,14,18,6,16,14,1,2,19],[6,14,20,14,14,14,5,17,19],[4,14,20,20,10,14,17,5,10],[4,5,12,17,20,5,18,4,8],[10,17,20,11,17,17,12,7,6],[17,19,20,12,8,19,9,7,17]]
result = Solution()
t = result.equalPairs(grid)
print(t)


