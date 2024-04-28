import os
os.system('clear')
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        i = 0
        lenArray = len(arr)
        count = []
        while i < lenArray:
            currentCount = 1
            while i+1 < lenArray and arr[i] == arr[i+1]:
                currentCount += 1
                i += 1
            i += 1
            count.append(currentCount)
        count.sort()
        i = 0
        lenCount = len(count)
        while i < lenCount - 1:
            if count[i] == count[i+1]:
                return False
            i += 1
        return True
    
arr = [1,2,2,1,1,3]
result = Solution()
t = result.uniqueOccurrences(arr)
print(t)