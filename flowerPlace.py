import os
os.system('clear')
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        countZero = 1
        maxN = 0
        for bed in flowerbed:
            if bed == 0:
                countZero += 1
            if bed == 1:
                countZero = 0
            if countZero == 3:
                maxN += 1
                countZero = 1
            if maxN == n:
                output = True
                return output

        if countZero == 2:
            maxN += 1
        if n > maxN:
            output = False
        else:
            output = True
        return output
# flowerbed = [1,0,0,0,0,0,1]
flowerbed = [0,0,1,0,1]
n = 1
result = Solution()
t = result.canPlaceFlowers(flowerbed, n)
print(t)