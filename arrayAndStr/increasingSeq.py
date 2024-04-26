import os
os.system('clear')
import numpy as np
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lenNum = 0
        lenUniq = 0
        newNums = []
        for i in range(0, len(nums)):
            num = nums[i]
            if num not in newNums:
                lenUniq += 1
            if i == 0:
                newNums.append(num)
                lenNum += 1
            elif num != nums[i-1]:
                newNums.append(num)
                lenNum += 1
            
        if lenUniq < 3:
            return False     
        newNums = np.array(newNums)  
        for i in range(0, lenNum):
            num1 = newNums[i]
            newNums2 = newNums[i+1:lenNum]
            idxNum2 = np.squeeze(np.argwhere(newNums2 > num1))
            if idxNum2.size < 2:
                continue
            else:
                for j in idxNum2:
                    j = int(j)
                    num2 = newNums2[j]
                    newNums3 = newNums2[j+1:len(newNums2)]
                    idxNum3 = np.argwhere(newNums3 > num2)
                    if idxNum3.size < 1:
                        continue
                    else:
                        for k in idxNum3:
                            num3 = newNums3[k]
                            if num2>num1 and num3>num2:
                                return True
        return False
            
nums = np.arange(10000,0,-1)
nums = [1,2,3,4,5]
nums = [20,100,10,12,5,13]
result = Solution()
t = result.increasingTriplet(nums)
print(t)