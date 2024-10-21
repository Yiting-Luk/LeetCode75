import heapq
def totalCost(costs, k, candidates):
    total_cost = 0
    left_heap = []
    right_heap = []
    n = len(costs)
    for i in range(candidates):
        heapq.heappush(left_heap, (costs[i], i))  # (cost, index)            
    # Add last 'candidates' workers to right heap
    for i in range(max(candidates, n - candidates), n):
        heapq.heappush(right_heap, (costs[i], i))  # (cost, index)
    left_pointer = candidates
    right_pointer = n - candidates - 1

    while left_pointer <= right_pointer and k: 
            if left_heap[0][0] <= right_heap[0][0] or not right_heap:
                cost, index = heapq.heappop(left_heap)
                heapq.heappush(left_heap, (costs[left_pointer], left_pointer))
                left_pointer += 1
            else:
                cost, index = heapq.heappop(right_heap)
                heapq.heappush(right_heap, (costs[right_pointer], right_pointer))
                right_pointer -= 1
            total_cost += cost
            k -= 1
    if k > 0:
        workers = []   
         # Add the remaining elements in left_heap and right_heap to workers
        while left_heap:
            heapq.heappush(workers, heapq.heappop(left_heap))
        while right_heap:
            heapq.heappush(workers, heapq.heappop(right_heap))
        
        # Also add any remaining workers in the unprocessed range
        for i in range(left_pointer, right_pointer + 1):
            heapq.heappush(workers, (costs[i], i))
    while k:  
        cost, index = heapq.heappop(workers)
        total_cost += cost
        k -= 1

    return total_cost

costs = [10,1,11,10]
k = 2
candidates = 1
result = totalCost(costs, k, candidates)
print(result)