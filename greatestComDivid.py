import os
os.system('clear')
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1+str2 != str2+str1:
            return ""
        
        len1 = len(str1)
        len2 = len(str2)
        if len1 == len2:
            return str1
        
        if len1 > len2:   
            diff = str1[len2:]
            return self.gcdOfStrings(diff, str2)
        diff = str2[len1:]
        return self.gcdOfStrings(diff, str1)


str1 = 'ABABAB'
str2 = 'ABAB'
result = Solution()
t = result.gcdOfStrings(str1, str2)
print(t)