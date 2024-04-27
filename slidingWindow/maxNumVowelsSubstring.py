import os
os.system('clear')
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ["a","e","i","o","u"]
        s = list(s)
        if k == 1:
            for vowel in vowels:
                if vowel in s:
                    return k
        else:
            firstStr = s[0:k]
            restStr = s
            max = 0
            count = []
            for currentS in firstStr:
                restStr.remove(currentS)
                if currentS in vowels:
                    count.append(1)
                else:
                    count.append(0)
            sumCount = sum(count)
            if sumCount > max:
                max = sumCount
                if max == k:
                    return max
            
            for currentS in restStr:
                if currentS in vowels:
                    count.append(1)
                    sumCount = sumCount - count[0] + 1
                else:
                    count.append(0)
                    sumCount = sumCount - count[0]      
                if sumCount > max:
                    max = sumCount
                    if max == k:
                        return max
                del count[0]        
            return max
            
s = "abciiidef"
s = "aeiou"
s = "lltmscqjyvimgevhydqrcejbvceldwullgufmtlylucvgfyjhzdigyvnxefaumrikmkdeneeomybuerca"
k = 9
result = Solution()
t = result.maxVowels(s, k)
print(t)
