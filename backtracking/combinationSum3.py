def combinationSum3(k, n):
    def backtrack(start, k, n, path, res):
        if k == 0 and n == 0:
            res.append(path[:])
            return
        
        if k < 0 and n < 0:
            return
        
        for i in range(start, 10):
            path.append(i)
            backtrack(i+1, k-1, n-i, path, res)
            path.pop() # allowing the algorithm to explore different possible paths.
    
    res = []
    backtrack(1, k, n, [], res)
    return res

k = 3
n = 7
print(combinationSum3(k, n))