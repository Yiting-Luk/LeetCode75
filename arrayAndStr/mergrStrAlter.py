import os
os.system('clear')
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)
        len2 = len(word2)
        lenAlter = min([len1, len2])
        output = []
        for i in range(lenAlter):
            char1 = word1[i]
            char2 = word2[i]
            output.append(char1)
            output.append(char2)
        if len1 > len2:
            output.append(word1[len2 : len1])
        if len2 > len1:
            output.append(word2[len1 : len2])
        result = "".join(output)
        print(word1)
        print(word2)
        print(result)
        return result

word1 = "abcet"
word2 = "pqr"
result = Solution()
result.mergeAlternately(word1, word2)

