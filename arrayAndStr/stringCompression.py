import os
os.system('clear')
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        idxComp = 1
        for i in range(0, len(chars)):
            if i == 0:
                priorLetter = chars[0]
                count = 1
            else:
                currentLetter = chars[i]
                if currentLetter == priorLetter:
                    count += 1
                else:
                    if count > 1:
                        if count < 10:
                            chars[idxComp] = str(count)
                            idxComp += 1
                        else:
                            temp = str(count)
                            for letter in temp:
                                chars[idxComp] = letter
                                idxComp += 1                       
                    count = 1
                    chars[idxComp] = currentLetter
                    idxComp += 1
                priorLetter = currentLetter
        if count > 1:
            if count < 10:
                chars[idxComp] = str(count)
                idxComp += 1
            else:
                temp = str(count)
                for letter in temp:
                    chars[idxComp] = letter
                    idxComp += 1   
        chars[idxComp:len(chars)] = []
        return len(chars)
chars = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
result = Solution()
t = result.compress(chars)
print(t)   