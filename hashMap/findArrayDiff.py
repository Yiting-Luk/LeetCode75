import os
os.system('clear')
import numpy as np
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        uniqNum1 = list(np.unique(nums1))
        uniqNum2 = list(np.unique(nums2))
        left = 0
        right = len(uniqNum1)-1
        while left <= right:
            num = uniqNum1[left]
            if num in uniqNum2:
                del uniqNum1[left]
                uniqNum2.remove(num)
                right -= 1
            else:
                left += 1
        answer.append(uniqNum1)
        answer.append(uniqNum2)
        return answer
    
nums1 = [1,2,3]
nums2 = [2,4,6]
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
result = Solution()
t = result.findDifference(nums1, nums2)
print(t)
