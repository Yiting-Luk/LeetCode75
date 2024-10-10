# There is only one way to travel between two different cities.
# Depth-first search or DFS algorithm traverses or explores data structures, such as trees and graphs.

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """       
        self.count = 0
        # look for the first connector including node 0
        def search0(connections):
            stack = []
            for i in range(0, len(connections)):
                if 0 in connections[i]:
                    self.path.append(connections[i])
                    if connections[i][0] == 0:
                        self.count += 1
                        temp = self.path[-1][0]
                        self.path[-1][0] = self.path[-1][1]
                        self.path[-1][-1] = temp
                    key = self.path[-1][0]
                    connections.pop(i)
                    break
                else:
                    stack.append(connections[i])
            if self.path == []:
                return stack
            else:
                stack = []
            for i in range(0, len(connections)):
                if key in connections[i] and 0 not in connections[i]:
                    self.path.append(connections[i])
                    if connections[i][0] == key:
                        self.count += 1
                        temp = self.path[-1][0]
                        self.path[-1][0] = self.path[-1][1]
                        self.path[-1][-1] = temp
                    key = self.path[-1][0]
                else:
                    stack.append(connections[i])
            return stack
        
        def search(connections):
            stack = []
            for i in range(0, len(connections)):
                if connections[i][0] not in self.visited and connections[i][1] not in self.visited:
                    stack.append(connections[i])
                else:
                    self.path.append(connections)
                    if connections[i][0] in self.visited:
                        self.count += 1
                        temp = self.path[-1][0]
                        self.path[-1][0] = self.path[-1][1]
                        self.path[-1][-1] = temp
                    key = self.path[0][0]
                    connections.pop(i)                    
            for i in range(0, len(connections)):
                if key in connections[i]:
                    self.path.append(connections[i])
                    if key in connections[i][0]:
                        self.count += 1   
                        temp = self.path[-1][0]
                        self.path[-1][0] = self.path[-1][1]
                        self.path[-1][-1] = temp
                    key = self.path[-1][0]
                else: stack.append(connections[i])    
            return stack
        
        self.visited = []
        while connections:
            self.path = []
            connections = search0(connections)
            if self.path == []:
                while connections:
                    self.path = []
                    connections = search(connections)
                    self.visited += self.path
                return
            else:
                self.visited += self.path
        return self.count
        
              
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]       
n = 10
connections = [[0,1],[2,1],[3,2],[0,4],[5,1],[2,6],[5,7],[3,8],[8,9]]
n = 5
connections = [[4,3],[2,3],[1,2],[1,0]]
obj = Solution()
result = obj.minReorder(n, connections)
print(result)