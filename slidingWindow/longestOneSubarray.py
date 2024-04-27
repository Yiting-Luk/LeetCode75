import os
os.system('clear')
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
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
        return result-k
nums = [1,1,0,1]
result = Solution()
t = result.longestSubarray(nums)
print(t)