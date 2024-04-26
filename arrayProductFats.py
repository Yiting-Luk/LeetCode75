import os
os.system('clear')
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lenNums = len(nums)
        # zeroLoc = []
        # nonZeroProduct = 1
        numZeros = 0
        prefix = [1]*lenNums
        surfix = [1]*lenNums
        for i in range(0, lenNums):
            if nums[i] == 0:
                # zeroLoc.append(i)
                numZeros +=1
            # else:
            #     nonZeroProduct = nonZeroProduct*nums[i]
            if i > 0:
                prefix[i] = prefix[i-1]*nums[i-1]
                surfix[lenNums-i-1] = surfix[lenNums-i]*nums[lenNums-i]

        # if len(zeroLoc) > 1:
        if numZeros > 1:
            product = [0]*lenNums
            return product

        # if len(zeroLoc) == 1:
        #     product = [0]*lenNums
        #     product[zeroLoc[0]] = nonZeroProduct
        #     return product
        
        # if not len(zeroLoc):
        else:
            product = []
            for i in range(0, lenNums):
                product.append(prefix[i]*surfix[i])
            return product

    
nums = [-1,1,0,-3,3]
nums = [1,2,3,4]
# nums = [0,0]
result = Solution()
t = result.productExceptSelf(nums)
print(t)