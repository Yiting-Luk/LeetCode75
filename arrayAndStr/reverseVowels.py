import os
os.system('clear')
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelDict = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowelS = [];
        idxDict = [];
        i = 0
        for letter in s:
            if letter in vowelDict:
                vowelS += letter
                idxDict.append(i)
            i += 1
        i = 0
        lenDict = len(vowelS) - 1
        vowelS = list(vowelS)
        s = list(s)
        for idx in idxDict:
            s[idx] = vowelS[lenDict - i]
            i += 1
        return "".join(s)
s = "leetcode"
result = Solution()
t = result.reverseVowels(s)
print(t)

