import os
os.system('clear')
from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        while t - self.q[0] > 3000:
            self.q.popleft()
        return len(self.q)


t = [[], [1], [100], [3001], [3002]]
result = []
for tt in t:
    if tt == []:
        obj = RecentCounter()
    else:
        tt = tt[0]
        result.append(obj.ping(tt))
print(result)
