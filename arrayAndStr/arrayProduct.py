import os
os.system('clear')
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lenNums = len(nums)
        zeroLoc = []
        nonZeroProduct = 1
        for i in range(0, lenNums):
            if nums[i] == 0:
                zeroLoc.append(i)
            else:
                nonZeroProduct = nonZeroProduct*nums[i]

        if len(zeroLoc) > 1:
            product = [0]*lenNums

        if len(zeroLoc) == 1:
            product = [0]*lenNums
            product[zeroLoc[0]] = nonZeroProduct

        if not len(zeroLoc):
            product = []
            for i in range(0, lenNums):
                currentProd = nonZeroProduct/nums[i]
                product.append(currentProd)

        return product
    
nums = [-1,1,0,-3,3]
# nums = [1,2,3,4]
# nums = [0,0]
result = Solution()
t = result.productExceptSelf(nums)
print(t)