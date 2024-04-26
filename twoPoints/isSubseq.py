import os
os.system('clear')
import numpy as np
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        locT = []
        foundLetter = 0
        idxT0 = 0
        for idxS in range(0, len(s)):
            letterS = s[idxS]
            for idxT in range(idxT0, len(t)):
                letterT = t[idxT]
                if letterT == letterS:
                    foundLetter = 1
                    locT.append(idxT)
                    idxT0 = idxT + 1
                    break
            if foundLetter == 0:
                return False
            foundLetter = 0
        return True
s = "abc"
t = "ahbgdc"
result = Solution()
t = result.isSubsequence(s, t)
print(t)