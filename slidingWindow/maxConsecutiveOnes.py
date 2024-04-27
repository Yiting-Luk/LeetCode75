import os
os.system('clear')
import numpy as np
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        currentSeq = []
        currentSeq.append(nums[0])
        lenCurrentSeq = 1
        result = k
        if nums[0] == 0:
            numZero = 1
        else:
            numZero = 0
        lenNums = len(nums)
        while right < lenNums-1:
            right += 1
            currentSeq.append(nums[right])
            lenCurrentSeq += 1
            if nums[right] == 0:
                numZero += 1
            if numZero <= k:
                result = max([result, lenCurrentSeq])
            while numZero > k:
                left += 1
                if currentSeq[0] == 0:
                    numZero -= 1
                del currentSeq[0]
                lenCurrentSeq -= 1
                
        return result
nums = [1,1,1,0,0,0,1,1,1,1,0]
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# nums = [0,0,1,1,1,0,0]
# nums = [1,1,1,0,0,0,1,1,1,1]
k = 3
result = Solution()
t = result.longestOnes(nums, k)
print(t)
