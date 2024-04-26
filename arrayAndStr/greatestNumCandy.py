import os
os.system('clear')
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = []
        currentMax = max(candies)
        gap = currentMax - extraCandies
        for candy in candies:
            if candy < gap:
                output.append(False)
            else:
                output.append(True)
        return output
    
candies = [2,3,5,1,3]
extraCandies = 3
result = Solution()
t = result.kidsWithCandies(candies, extraCandies)
print(t)