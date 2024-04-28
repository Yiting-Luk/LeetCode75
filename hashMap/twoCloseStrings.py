import os
os.system('clear')
import numpy as np
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word1 = sorted(word1)
        word2 = sorted(word2)
        i = 0
        len1 = len(word1)
        len2 = len(word2)
        uniqWord1 = []
        uniqWord2 = []
        count1 = []
        count2 = []
        while i < len1:
            count = 1
            while i+1 < len1  and word1[i] == word1[i+1]:
                count += 1
                i += 1
            uniqWord1.append(word1[i])
            count1.append(count)
            i += 1
        i = 0
        while i < len2:
            count = 1
            while i+1 < len2  and word2[i] == word2[i+1]:
                count += 1
                i += 1
            uniqWord2.append(word2[i])
            count2.append(count)
            i += 1
        count1.sort()
        count2.sort()
        if count1 == count2 and uniqWord1 == uniqWord2:
            return True
        else:
            return False

word1 = "a"
word2 = "aa"
result = Solution()
t = result.closeStrings(word1, word2)
print(t)
