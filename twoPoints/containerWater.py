import os
os.system('clear')
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        numCon = len(height)
        for idxLeft in range(0, numCon):
            if height[idxLeft] != 0:
                steps = int(max/height[idxLeft])  
                for idxRight in range(idxLeft+steps, numCon):
                    currentArea = (idxRight - idxLeft)*min([height[idxLeft], height[idxRight]])
                    if currentArea > max:
                        max = currentArea
        return max
            

height = [1,8,6,2,5,4,8,3,7]
result = Solution()
t = result.maxArea(height)
print(t)