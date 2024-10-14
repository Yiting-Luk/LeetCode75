from collections import defaultdict

def calcEquation(equations, values, queries):
    # Step 1: Build the graph
    graph = defaultdict(dict)
    
    for (A, B), value in zip(equations, values): # zip() is used to combine the equations list and the values list. 
        # This makes it easy to loop through both equations and values at the same time. 
        # equations[i] = [Ai, Bi]
        # values[i] = value
        graph[A][B] = value 
        # A is a node in the graph. B is a neighbor of A. graph[A][B] stores the weight of the edge from node A to node B.
        graph[B][A] = 1.0 / value  

    # Step 2: Function to perform DFS and find the result for a query
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)
        for neighbor, val in graph[start].items():
            if neighbor in visited:
                continue # skip the rest of the current iteration of for or while loops.
            result = dfs(neighbor, end, visited)
            if result != -1.0:
                return result * val
        return -1.0
    
    # Step 3: Process each query
    results = []
    for C, D in queries:
        if C in graph and D in graph:
            results.append(dfs(C, D, set())) # set() is en empty set passed to the dfs.
        else:
            results.append(-1.0)
    
    return results

# Example usage:
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

output = calcEquation(equations, values, queries)
print(output)
