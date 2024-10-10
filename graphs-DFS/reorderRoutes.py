class Solution(object):
    def minReorder(self, n, connections):
        from collections import defaultdict

        # Step 1: Build the graph
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # Edge from a to b (current direction)
            graph[b].append((a, -1)) # Edge from b to a (reversed direction)

        # Step 2: DFS traversal to count needed reversals
        def dfs(city, parent):
            change_count = 0
            for neighbor, direction in graph[city]:
                if neighbor == parent:
                    continue
                # If the direction is 1, we need to change it
                if direction == 1:
                    change_count += 1
                change_count += dfs(neighbor, city)
            return change_count

        # Start DFS from city 0
        return dfs(0, -1)

# Example usage:
n = 6
connections = [[4, 5], [0, 1], [1, 3], [2, 3], [4, 0]]
obj = Solution()
result = obj.minReorder(n, connections)
print(result)
