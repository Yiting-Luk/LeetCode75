import os
os.system('clear')
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = []
        i = 0
        while "[" in s:
            letter = s[i]
            if ord(letter) == 91:
                leftIdx = i
            if ord(letter) == 93:
                rightIdx = i
                idxNum = leftIdx-1
                letter = s[idxNum]
                while ord(letter) <= 57:
                    num.append(letter)
                    idxNum -= 1
                    letter = s[idxNum]
                if len(num) > 0:
                    num.reverse()
                    count = int("".join(num))
                else: 
                    count = 1
                leftStr = s[0:idxNum+1]
                midStr = s[leftIdx+1:rightIdx]*count
                rightStr = s[rightIdx+1:]
                s = leftStr + midStr + rightStr
                i = -1
                num = []
            i += 1
        return s

s = "3[a2[c]]"
s = "100[leetcode]"
# s = "2[abc]3[cd]ef"
result = Solution()
t = result.decodeString(s)
print(t)
