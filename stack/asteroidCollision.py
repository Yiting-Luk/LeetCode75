class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        lenStack = 0
        flag = 1
        for asteroid in asteroids:
            if lenStack == 0:
                stack.append(asteroid)
                lenStack += 1
            else:
                lastSign = stack[-1] > 0
                currentSign = asteroid > 0
                while lenStack > 0 and lastSign and not currentSign:                   
                    lastSize = abs(stack[-1])
                    currentSize = abs(asteroid)
                    if lastSize == currentSize:
                        stack.pop()
                        lenStack -= 1
                        flag = 0
                        break
                    elif lastSize > currentSize:
                        flag = 0
                        break
                    else:
                        stack.pop()
                        lenStack -= 1
                        if lenStack > 0:
                            lastSign = stack[-1] > 0 
                        else:
                            break
                if flag:
                    stack.append(asteroid)
                    lenStack += 1
                flag = 1
        return stack

asteroids = [5,10,-5]
asteroids = [10,2,-5]
asteroids = [-2,-1,1,2]
asteroids = [-2,-2,1,-2]
asteroids = [8,-8]
result = Solution()
t = result.asteroidCollision(asteroids)
print(t)