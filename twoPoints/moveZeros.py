import os
os.system('clear')
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonZeroCount = 0
        i = 0
        zeroCount = 0
        currentJ = []
        while i < len(nums):
            num = nums[i]
            if num == 0:
                zeroCount += 1
                if currentJ:
                    j = currentJ+1
                else: 
                    j = i+1
                while j < len(nums):
                    num = nums[j]
                    if num != 0:
                        nums[nonZeroCount] = num
                        nums[j] = 0
                        nonZeroCount += 1
                        currentJ = j
                        break
                    j += 1
            else:
                nonZeroCount += 1
            i += 1
        return nums
    
nums = [0,1,0,3,12]
nums = [1]
nums = [0,1]
# nums = [2,1]
nums = [0,1,1,0]
result = Solution()
t = result.moveZeroes(nums)
print(t)