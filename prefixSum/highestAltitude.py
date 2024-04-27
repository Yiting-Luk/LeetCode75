import os
os.system('clear')
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        currentAltitude = 0
        maxAltitude = 0
        for currentGain in gain:
            nextAltitude = currentGain + currentAltitude
            currentAltitude = nextAltitude
            maxAltitude = max([maxAltitude, nextAltitude])
        return maxAltitude

gain = [-5,1,5,0,-7]
result = Solution()
t = result.largestAltitude(gain)
print(t)