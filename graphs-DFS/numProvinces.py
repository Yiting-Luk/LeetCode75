# A province is a group of directly or indirectly connected cities.
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(provinces, city):
            for i in range(0, len(provinces)):
                if city in provinces[i]:
                    return i
        numCity = len(isConnected)
        provinces = []
        for i in range(0, numCity):
            provinces.append([i])
        for i in range(0, numCity):
            for j in range(i, numCity):
                if isConnected[i][j] == 1:
                    p = dfs(provinces, i)
                    q = dfs(provinces, j)
                    if p != q:
                        if p < q:
                            temp = provinces[q]
                            provinces.pop(q)
                            provinces[p] += temp
                            
                        else:
                            temp = provinces[p]
                            provinces.pop(p)
                            provinces[q] += temp                           
        return len(provinces)
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
obj = Solution()
result = obj.findCircleNum(isConnected)
print(result)
