import os
os.system("clear")
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        victory = None
        i = 0
        senate0 = list(senate)
        while victory is None:
            # print(senate0)
            senator = senate0[i]
            if senator == 'R':
                enemy = 'D'
            else:
                enemy = 'R'
            if enemy not in senate0:
                victory = senator
            else:
                flag = 1
                j = i+1
                if j > len(senate0)-1:
                    j = 0
                while flag:
                    if senate0[j] == enemy:         
                        del senate0[j]
                        flag = 0
                    else:
                        j += 1
                        if j > len(senate0)-1:
                            j = 0
                if j > i:
                    i += 1
                if i > len(senate0)-1:
                    i = 0
        if victory == 'R':
            return  "Radiant"
        elif victory == 'D':
            return "Dire"
   
senate ="DRRDRDRDRDDRDRDR"
senate = "RDD"
obj = Solution()
result = obj.predictPartyVictory(senate)
print(result)