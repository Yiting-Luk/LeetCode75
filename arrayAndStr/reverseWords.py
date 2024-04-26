import os
os.system('clear')
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitS = s.split()
        numChar = len(splitS)
        reversdS = [None]*numChar
        for i in range(0, numChar):
            reversdS[numChar - i - 1] = splitS[i]
        return " ".join(reversdS)

s = "the sky is blue"
result = Solution()
t = result.reverseWords(s)
print(t)