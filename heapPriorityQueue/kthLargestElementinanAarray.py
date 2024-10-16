import heapq
def findKthLargest(nums, k):
    heap = nums[:k] # create a min-heap with the first k elements
    heapq.heapify(heap) # In a min-heap, the smallest element is always at the root (the first element in the list), 
    # and every parent node is smaller than or equal to its children. 

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num) # When you call heapq.heappushpop(heap, item), 
            # the function first pushes item onto the heap and then immediately pops the smallest element.
    
    return heap[0] 

nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(findKthLargest(nums1, k1))  # Output: 5