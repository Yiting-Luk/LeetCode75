class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = [0]
        i = 0
        while i < len(keys):
            newKeys = rooms[keys[i]]
            for curr_key in newKeys:
                if curr_key not in keys:
                    keys.append(curr_key)
            i += 1
        if len(keys) == len(rooms):
            return True
        else:
            return False

rooms = [[1,3],[3,0,1],[2],[0]]
rooms = [[2],[],[1]]
obj = Solution()
result = obj.canVisitAllRooms(rooms)
print(result)