import os
os.system('clear')
from collections import Counter
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        counter = Counter(nums)
        uniqNum = list(counter.keys())
        uniqCount = list(counter.values())
        left = 0
        right = len(uniqNum)-1
        numPairs = 0
        while left <= right:
            twoSum = uniqNum[left] + uniqNum[right]
            if twoSum == k:
                if left < right:
                    countLeft = uniqCount[left]
                    countRight = uniqCount[right]
                    numPairs += min([countLeft, countRight])
                else:
                    countLeft = uniqCount[left]
                    numPairs += int(countLeft/2)
                left += 1
                right -=1
            elif twoSum < k:
                left += 1
            elif twoSum > k:
                right -=1
        return numPairs
    
nums = [1,2,3,4]
# nums = [3,1,3,4,3]
# nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
nums = [64,35,69,79,76,60,58,38,3,81,74,9,77,21,54,54,14,72]
k = 47
result = Solution()
t = result.maxOperations(nums, k)
print(t)