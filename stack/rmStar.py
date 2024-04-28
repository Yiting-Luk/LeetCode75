import os
os.system('clear')
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char != "*":
                stack.append(char)
            else:
                if stack[-1] and char == "*":
                    stack.pop()
        return "".join(stack)
    
s = "leet**cod*e"
s = "erase*****"
s = "u*ensso****x*q"
result = Solution()
t = result.removeStars(s)
print(t)
