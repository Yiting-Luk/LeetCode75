import os
os.system('clear')
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        lenNums = len(nums)
        if lenNums == k:
            return sum(nums)/float(k)
        else:
            max = sum(nums[0:k])
            left = 1
            right = left + k - 1
            currentSum = max
            while right < len(nums):
                currentSum = currentSum - nums[left-1] + nums[right]
                if currentSum > max:
                    max = currentSum
                left += 1
                right += 1
            return max/float(k)

nums = [1,12,-5,-6,50,3]
nums = [0,1,1,3,3]
nums = [0,4,0,3,2]
k = 2
result = Solution()
t = result.findMaxAverage(nums, k)
print(t)
