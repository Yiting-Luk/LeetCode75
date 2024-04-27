import os
os.system('clear')
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = -1
        pivotIndex = -1
        while i < len(nums)-1:
            i += 1
            if i == 0:
                prefixSum = 0
                surfixSum = sum(nums[1:len(nums)])
            elif i == len(nums)-1:
                prefixSum = prefixSum + nums[i-1]
                surfixSum = 0
            else:
                prefixSum = prefixSum + nums[i-1]
                surfixSum = surfixSum - nums[i]
            if prefixSum == surfixSum:
                pivotIndex = i
                return pivotIndex
        return pivotIndex
nums = [1,7,3,6,5,6]
nums = [-1,-1,0,1,0,1]
result = Solution()
t = result.pivotIndex(nums)
print(t)
